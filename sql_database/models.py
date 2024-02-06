from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
metadata = MetaData()
Base = declarative_base(metadata = metadata)

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

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique=True)
    midi_hotkey = Column(String, nullable=True)
    sorting = Column(Integer, nullable=True)
    associations = relationship('Association')
    def __repr__(self):
        return f'{self.name}'


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, index = True)
    friendly_name = Column(String, nullable=True)
    filename = Column(String, nullable=True)
    location = Column(String)
    # def __repr__(self):
    #     return self.location


class Association(Base):
    __tablename__ = 'association'

    id = Column(Integer, primary_key=True, index = True)
    mood_id = Column(Integer, ForeignKey('mood.id'), nullable=False)
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False)
    track = relationship('Track', uselist=False)
    # def __repr__(self):
    #     return self.track