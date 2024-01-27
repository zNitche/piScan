from alembic import command, config
import os
import shutil


def get_config(migrations_dir, db_engine):
    cfg = config.Config(os.path.join(migrations_dir, "alembic.ini"))

    cfg.set_main_option("sqlalchemy.url", str(db_engine.url))
    cfg.set_main_option("script_location", migrations_dir)
    cfg.set_main_option("compare_type", "true")

    return cfg


def init_migrations(app_config, db_engine):
    migrations_dir = getattr(app_config, "MIGRATIONS_DIR_PATH")

    if not os.path.exists(migrations_dir):
        cfg = get_config(migrations_dir, db_engine)

        command.init(cfg, migrations_dir)
        command.stamp(cfg, "head")

        env_template_path = os.path.join("piScan", "database", "alembic_template", "env.template.py")

        shutil.copy2(os.path.join(getattr(app_config, "CURRENT_DIR"), env_template_path),
                     os.path.join(migrations_dir, "env.py"))


def migrate(app_config, db_engine):
    alembic_config = get_config(getattr(app_config, "MIGRATIONS_DIR_PATH"), db_engine)

    with db_engine.begin() as connection:
        alembic_config.attributes["connection"] = connection

        command.revision(alembic_config, autogenerate=True)
        command.upgrade(alembic_config, "head")
