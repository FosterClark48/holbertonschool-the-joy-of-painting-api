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
  colors = relationship('Color', secondary='EpisodeColors', back_populates='episodes')
  subject_matters = relationship('SubjectMatter', secondary='EpisodeSubjectMatter', back_populates='episodes')
