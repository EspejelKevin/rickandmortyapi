from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):
    # SERVICE
    SERVICE_NAME: str = 'RickAndMortyAPI'
    RELOAD: bool = False
    PORT: int = 8000
    HOST: str = '0.0.0.0'
    NAMESPACE: str
    API_VERSION: str = 'v1'
    RESOURCE: str
    SYNC_EPISODES: bool = False

    # DATABASE
    URL_DATABASE: str

    # EXTERNAL API
    RICK_MORTY_API_URL: str
    TIMEOUT: float = 30.0


@lru_cache()
def get_settings() -> Settings:
    return Settings()