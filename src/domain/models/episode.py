from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Boolean

from datetime import date

from .base import Base



class Episode(Base):
    __tablename__ = 'episodes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    episode: Mapped[str] = mapped_column(String(20))
    air_date: Mapped[date] = mapped_column(Date)
    favorite: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f'Episode(id={self.id}, name={self.name}, episode={self.episode})'
