from piScan.database.migrations import init_migrations, migrate
from piScan.database.db import Database
from config import Config


def main():
    db = Database()
    db.init_db(Config.DATABASE_URI)

    init_migrations(Config, db.engine)
    migrate(Config, db.engine)


if __name__ == '__main__':
    main()
