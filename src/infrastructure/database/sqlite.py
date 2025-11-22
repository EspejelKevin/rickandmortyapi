from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from domain import get_settings


settings = get_settings()


class SQLite:
    _engine = create_engine(settings.URL_DATABASE)

    def __init__(self):
        _sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        self._session: Session = _sessionlocal()

    def __enter__(self):
        return self
    
    def get_session(self):
        return self._session
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:
            self._session.commit()
        else:
            self._session.rollback()
