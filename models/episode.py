from .base import Base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship


class Episode(Base):
  __tablename__ = 'Episodes'

  EpisodeID = Column(String(10), primary_key=True)
  Title = Column(String(255))
  SeasonNumber = Column(Integer)
  EpisodeNumber = Column(Integer)
  AirDate = Column(Date)

  # Relationships
  episode_colors = relationship("EpisodeColor", back_populates="episode")
  episode_subject_matters = relationship("EpisodeSubjectMatter", back_populates="episode")
