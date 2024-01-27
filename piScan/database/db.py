# It will work just fine if we choose following implementation
# https://flask.palletsprojects.com/en/3.0.x/patterns/sqlalchemy/
# but I wanted to add layer of abstraction in case of future use

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import exc

Base = declarative_base()


class Database:
    def __init__(self):
        self.engine = None
        self.session_maker = None
        self.session = None

    def init_db(self, db_uri):
        self.engine = create_engine(db_uri)
        self.session_maker = self.__create_session_maker()
        self.session = self.get_session()

    def create_all(self):
        from piScan import models
        Base.metadata.create_all(bind=self.engine)

    def __create_session_maker(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return scoped_session(self.session_maker)

    def close_session(self, exception=None):
        session = self.get_session()

        if isinstance(exception, exc.SQLAlchemyError):
            session.rollback()

        session.remove()

    @contextmanager
    def session_context(self):
        session = self.get_session()

        try:
            yield session

        except Exception as e:
            session.rollback()
            raise

        finally:
            session.remove()
