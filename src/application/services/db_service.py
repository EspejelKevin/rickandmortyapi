from domain import DBRepository


class DBService(DBRepository):
    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    def get_episodes(self):
        return self.db_repository.get_episodes()
    
    def get_episode_by_id(self, id):
        return self.db_repository.get_episode_by_id(id)
    
    def get_episode_by_code(self, code):
        return self.db_repository.get_episode_by_code(code)
        
    def create_episode(self, episode):
        return self.db_repository.create_episode(episode)
    
    def update_episode(self, id, episode):
        return self.db_repository.update_episode(id, episode)
    
    def delete_episode_by_id(self, id):
        return self.db_repository.delete_episode_by_id(id)
    
    def rollback(self):
        return self.db_repository.rollback()
