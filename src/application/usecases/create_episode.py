from fastapi import status

from datetime import datetime
import uuid


from domain import (DBRepository, EpisodeInput, EpisodeDTO,
                    ResourceAlreadyExistsError, InternalServerError, Response)
from log import Log


class CreateEpisode:
    def __init__(self, db_service: DBRepository, log: Log):
        self.db_service = db_service
        self.log = log
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.meta = {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}

    def execute(self, episode_input: EpisodeInput):
        self.log.info('start logic create_episode')

        episode_db = self.db_service.get_episode_by_code(episode_input.episode)

        if episode_db:
            self.log.info('resource already exists in database', extra={'details': {'episode': episode_input.name}})
            raise ResourceAlreadyExistsError(resource=episode_input.name, meta=self.meta)
        
        episode_dto = EpisodeDTO(name=episode_input.name, episode=episode_input.episode, air_date=episode_input.air_date)
        _id = self.db_service.create_episode(episode_dto)

        if not _id:
            message = f'error while creating episode {episode_input.name}'
            raise InternalServerError(message=message, meta=self.meta)
        
        episode_dto.id = _id

        self.log.info('episode created with success')
        
        return Response(data=episode_dto, meta=self.meta, status_code=status.HTTP_201_CREATED)
