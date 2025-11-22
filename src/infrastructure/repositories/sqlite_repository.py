from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from domain import DBRepository, Episode


class SQLiteRepository(DBRepository):
    def __init__(self, database):
        self.database = database

    def get_episodes(self):
        with self.database() as sqlite:
            session: Session = sqlite.get_session()
            return session.scalars(select(Episode).order_by(Episode.id)).all()
    
    def get_episode_by_id(self, id):
        with self.database() as sqlite:
            session: Session = sqlite.get_session()
            return session.scalars(select(Episode).where(Episode.id==id)).one_or_none()
    
    def get_episode_by_code(self, code):
        with self.database() as sqlite:
            session: Session = sqlite.get_session()
            return session.scalars(select(Episode).where(Episode.episode==code)).one_or_none()
        
    def create_episode(self, episode):
        try:
            with self.database() as sqlite:
                session: Session = sqlite.get_session()
                new_episode = Episode(name=episode.name, episode=episode.episode, air_date=episode.air_date)
                session.add(new_episode)
                session.flush()
                session.refresh(new_episode)
                return new_episode.id
        except Exception:
            return False
    
    def update_episode(self, id, episode):
        try:
            with self.database() as sqlite:
                session: Session = sqlite.get_session()
                session.execute(update(Episode).where(Episode.id==id).values(favorite=episode.favorite))
                return True
        except Exception:
            return False
    
    def delete_episode_by_id(self, id):
        try:
            with self.database() as sqlite:
                session: Session = sqlite.get_session()
                session.execute(delete(Episode).where(Episode.id==id))
                return True
        except Exception:
            return False

    def rollback(self):
        with self.database() as sqlite:
            session: Session = sqlite.get_session()
            session.rollback()
