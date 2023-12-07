from .base import Base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship


class SubjectMatter(Base):
  __tablename__ = 'SubjectMatter'

  SubjectID = Column((Integer), primary_key=True, autoincrement=True)
  SubjectName = Column(String(255))

  # Relationship
  episodes = relationship('Episode', secondary='EpisodeSubjectMatter', back_populates='subject_matters')
