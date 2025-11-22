from pydantic import BaseModel, Field

from datetime import date


class EpisodeInput(BaseModel):
    name: str = Field(min_length=5, max_length=80)
    episode: str = Field(pattern=r'^S\d{2}E\d{2}$')
    air_date: date


class EpisodeFavoriteInput(BaseModel):
    favorite: bool
