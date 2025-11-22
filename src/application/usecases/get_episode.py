from fastapi import status

from datetime import datetime
import uuid


from domain import DBRepository, ResourceNotFoundError, EpisodeDTO, Response
from log import Log


class GetEpisode:
    def __init__(self, db_service: DBRepository, log: Log):
        self.db_service = db_service
        self.log = log
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.meta = {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}

    def execute(self, _id):
        self.log.info('start logic get_episode')

        episode_db = self.db_service.get_episode_by_id(_id)

        if not episode_db:
            self.log.info('resource not found in database', extra={'details': {'episode_id': _id}})
            raise ResourceNotFoundError(resource=_id, meta=self.meta)
        
        episode_dto = EpisodeDTO(id=_id, name=episode_db.name, episode=episode_db.episode,
                                 air_date=episode_db.air_date.strftime('%B %d, %Y'), favorite=episode_db.favorite)
        
        self.log.info('episode got with success')
        
        return Response(data=episode_dto, meta=self.meta, status_code=status.HTTP_200_OK)
