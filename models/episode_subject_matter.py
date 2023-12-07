from .base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class EpisodeSubjectMatter(Base):
  __tablename__ = 'EpisodeSubjectMatter'

  EpisodeID = Column(String(10), ForeignKey('Episodes.EpisodeID'), primary_key=True)
  SubjectID = Column(Integer, ForeignKey('SubjectMatter.SubjectID'), primary_key=True)

  # Relationships
  episode = relationship("Episode", back_populates="subject_matters")
  subject_matter = relationship("SubjectMatter", back_populates="episodes")
