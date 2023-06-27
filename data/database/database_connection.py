from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loguru import logger
from project_config.db_config import DatabaseConfig


class DatabaseConnection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.engine = None
        self.SQLSession = None

        self.connect_database()

    def connect_database(self):
        BASE_URL: str = f"postgresql+psycopg2://{self.config.USER}:{self.config.PASSWORD}@{self.config.HOST}:" \
                        f"{self.config.PORT}/{self.config.NAME}"

        try:
            self.engine = create_engine(BASE_URL)
            self.SQLSession = sessionmaker(bind=self.engine)
            logger.success("database connection succes")
        except Exception as ex:
            logger.critical("db didnt connected")
            raise ex

