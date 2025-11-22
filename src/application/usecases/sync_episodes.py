from fastapi import status

from datetime import datetime
import uuid
import httpx
import asyncio

from domain import DBRepository, EpisodeDTO, Response, get_settings, InternalServerError
from log import Log


class SyncEpisodes:
    def __init__(self, db_service: DBRepository, log: Log):
        self.db_service = db_service
        self.log = log
        self.settings = get_settings()
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.meta = {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}

    def execute(self):
        self.log.info('start logic sync_episodes')
        data = {'message': 'synchronization already completed'}

        if not self.settings.SYNC_EPISODES:
            coroutine = self.get_episodes()
            asyncio.run(coroutine)
            data['message'] = 'synchronization completed'
                    
        self.log.info('sync of episodes with success')
        self.settings.SYNC_EPISODES = True
    
        return Response(data=data, meta=self.meta, status_code=status.HTTP_201_CREATED)
    
    async def get_episodes(self):
        next_url = self.settings.RICK_MORTY_API_URL
        async with httpx.AsyncClient(timeout=self.settings.TIMEOUT) as client:
            while next_url:
                try:
                    response = await client.get(next_url)
                    response.raise_for_status()
                    data = response.json()
                    episodes = data.get('results', [])

                    for episode in episodes:
                        existing_episode = self.db_service.get_episode_by_id(episode.get('id', 0))

                        if existing_episode is None:
                            episode_dto = EpisodeDTO(
                                id=episode['id'],
                                name=episode['name'],
                                episode=episode['episode'],
                                air_date=datetime.strptime(episode["air_date"], '%B %d, %Y').date()
                            )

                            self.db_service.create_episode(episode_dto)
                    
                    next_url = data['info']['next']
                
                except Exception as e:
                    self.log.info(str(e))
                    self.db_service.rollback()
                    message = 'error while processing episodes from api'
                    raise InternalServerError(message=message, meta=self.meta)
