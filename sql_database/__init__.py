from sqlalchemy import MetaData, select
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Mood, Track, Association
from sqlalchemy.exc import SQLAlchemyError
from logging import Logger
from .models import Mood, Association, Track, metadata


def remake_db():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def create(logger:Logger, object, db:Session=SessionLocal()):
    try:
        db.add(object)
        db.commit()
        logger.info('committed data to db')
    except SQLAlchemyError as e:
        db.rollback()
        logger.warn(e)
    finally:
        db.close()


def get_moods(logger:Logger, db:Session=SessionLocal()):
    moods = [mood for mood in db.query(Mood).all()]

    return moods