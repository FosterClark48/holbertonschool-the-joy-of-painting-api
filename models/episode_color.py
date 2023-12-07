from .base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class EpisodeColor(Base):
  __tablename__ = 'EpisodeColors'

  EpisodeID = Column(String(10), ForeignKey('Episodes.EpisodeID'), primary_key=True)
  ColorID = Column(Integer, ForeignKey('Colors.ColorID'), primary_key=True)

  # Relationships
  episode = relationship("Episode", back_populates="episode_colors")
  color = relationship("Color", back_populates="episode_colors")
