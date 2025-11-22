from abc import ABCMeta, abstractmethod

from ..dto.episode import EpisodeDTO


class DBRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_episodes(self):
        raise NotImplementedError

    @abstractmethod
    def get_episode_by_id(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def get_episode_by_code(self, code: str):
        raise NotImplementedError
    
    @abstractmethod
    def create_episode(self, episode: EpisodeDTO):
        raise NotImplementedError
    
    @abstractmethod
    def update_episode(self, id: str, episode: EpisodeDTO):
        raise NotImplementedError
    
    @abstractmethod
    def delete_episode_by_id(self, id: str):
        raise NotImplementedError
