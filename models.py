from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

'''
Objects
    Mood
    Track
    Association
Relationships
    Association
        One Mood, One Track
'''

class Mood(Base):
    __tablename__ = 'mood'

    id = Column(BigInteger, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    midi_hotkey = Column(String, nullable=True)
    sorting = Column(Integer, nullable=True)


class Track(Base):
    __tablename__ = 'track'

    id = Column(BigInteger, primary_key=True, index=True, unique=True)
    location = Column(String)


class Association(Base):
    __tablename__ = 'association'

    id = Column(BigInteger, primary_key=True, index=True, unique=True)
    mood_id = Column(BigInteger, ForeignKey('mood.id'), nullable=False)
    track_id = Column(BigInteger, ForeignKey('track.id'), nullable=False)