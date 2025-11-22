from pydantic import BaseModel

from datetime import date


class EpisodeDTO(BaseModel):
    id: int | None = None
    name: str
    episode: str
    air_date: date | str
    favorite: bool = False
