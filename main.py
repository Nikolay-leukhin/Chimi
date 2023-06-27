from data.database.database import Database
from project_config.config import load_config, Config


def main():
    config: Config = load_config()
    db: Database = Database(config.db)


if __name__ == '__main__':
    main()