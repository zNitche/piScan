from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

Base = declarative_base()


class Database:
    def __init__(self):
        self.engine = None

    def init_db(self, db_uri):
        self.engine = create_engine(db_uri)

    def create_all(self):
        from piScan import models
        Base.metadata.create_all(bind=self.engine)

    def __create_session(self):
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=self.engine))

        return db_session

    @contextmanager
    def session(self):
        session = self.__create_session()

        try:
            yield session
            session.commit()

        except Exception as e:
            session.rollback()
            raise

        finally:
            session.remove()
