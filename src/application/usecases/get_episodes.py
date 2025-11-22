from fastapi import status

from datetime import datetime
import uuid


from domain import DBRepository, EpisodeDTO, Response
from log import Log


class GetEpisodes:
    def __init__(self, db_service: DBRepository, log: Log):
        self.db_service = db_service
        self.log = log
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.meta = {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}

    def execute(self):
        self.log.info('start logic get_episodes')

        episodes_db = self.db_service.get_episodes()

        episodes_dto = [EpisodeDTO(id=episode_db.id, name=episode_db.name, episode=episode_db.episode,
                                 air_date=episode_db.air_date, favorite=episode_db.favorite) for episode_db in episodes_db]
        
        self.log.info('episodes got with success')
        
        return Response(data=episodes_dto, meta=self.meta, status_code=status.HTTP_200_OK)
