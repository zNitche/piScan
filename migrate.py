from piScan.database.migrations import init_migrations, migrate
from piScan.database.db import Database
from config import Config


def main():
    db = Database()
    db.setup(Config.DATABASE_URI)

    init_migrations(Config.MIGRATIONS_DIR_PATH, db.engine)
    migrate(Config.MIGRATIONS_DIR_PATH, db.engine)


if __name__ == '__main__':
    main()
