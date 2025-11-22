from fastapi import status

from datetime import datetime
import uuid


from domain import (DBRepository, ResourceNotFoundError,
                    InternalServerError, Response)
from log import Log


class DeleteEpisode:
    def __init__(self, db_service: DBRepository, log: Log):
        self.db_service = db_service
        self.log = log
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.meta = {'transaction_id': self.transaction_id, 'timestamp': self.timestamp}

    def execute(self, _id):
        self.log.info('start logic delete_episode')

        episode_db = self.db_service.get_episode_by_id(_id)

        if not episode_db:
            self.log.info('resource not found in database', extra={'details': {'episode_id': _id}})
            raise ResourceNotFoundError(resource=_id, meta=self.meta)
        
        result = self.db_service.delete_episode_by_id(_id)

        if not result:
            message = f'error while deleting episode {_id}'
            raise InternalServerError(message=message, meta=self.meta)
        
        data = {'message': f'episode deleted with success: {_id}'}

        self.log.info('episode deleted with success')
        
        return Response(data=data, meta=self.meta, status_code=status.HTTP_200_OK)
