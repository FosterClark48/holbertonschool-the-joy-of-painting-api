from .base import Base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship


class Color(Base):
  __tablename__ = 'Colors'

  ColorID = Column((Integer), primary_key=True, autoincrement=True)
  ColorName = Column(String(50))
  ColorHexCode = Column(String(7))

  # Relationship
  episodes = relationship('Episode', secondary='EpisodeColors', back_populates='colors')
