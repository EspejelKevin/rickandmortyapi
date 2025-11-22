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

    # DATABASE
    URL_DATABASE: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()