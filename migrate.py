from piScan.database.migrations import init_migrations, migrate
from config import Config
from piScan.database.db import db_engine, init_db


def main():
    init_db()

    init_migrations(Config, db_engine)
    migrate(Config, db_engine)


if __name__ == '__main__':
    main()
