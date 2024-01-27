from piScan.database.migrations import init_migrations, migrate
from config import Config
from piScan.database.db import db_engine


def main():
    from piScan import models

    init_migrations(Config, db_engine)
    migrate(Config, db_engine)


if __name__ == '__main__':
    main()
