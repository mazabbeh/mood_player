from sqlalchemy import MetaData, select
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Mood, Track, Association
from sqlalchemy.exc import SQLAlchemyError
from logging import Logger
from .models import Mood, Association, Track, metadata
from shared_utils import setup_logger
logger = setup_logger('sql_database', 'logs/sql_database.log')

def remake_db():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def create(object, db:Session=SessionLocal(), logger:Logger=logger, reraise=False):
    try:
        db.add(object)
        db.commit()
        logger.info('committed data to db')
    except SQLAlchemyError as e:
        db.rollback()
        logger.warn(e)
        if reraise: raise SQLAlchemyError
    finally:
        db.close()


def get_moods(logger:Logger=logger, db:Session=SessionLocal()):
    moods = [str(mood) for mood in db.query(Mood).all()]
    return moods