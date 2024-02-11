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

    def setup(self, db_uri):
        self.engine = create_engine(db_uri)
        self.session_maker = self.__create_session_maker()
        self.session = self.get_session()

    def create_all(self):
        from piScan import models
        from piScan.database import events

        Base.metadata.create_all(bind=self.engine)

    def __create_session_maker(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return scoped_session(self.session_maker)

    def close_session(self, exception=None):
        if self.session:
            if isinstance(exception, exc.SQLAlchemyError):
                self.session.rollback()

            self.session.remove()

    def update_instance(self, instance, update_dict):
        for key, value in update_dict.items():
            setattr(instance, key, value)

        self.session.commit()

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
