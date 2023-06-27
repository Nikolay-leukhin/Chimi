from data.database.database_access import DatabaseAccess
from data.database.database_connection import DatabaseConnection
from data.models.models import Base
from project_config.db_config import DatabaseConfig


class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, config: DatabaseConfig):
        self.conn = DatabaseConnection(config)
        self.cursor = DatabaseAccess(self.conn)

        Base.metadata.create_all(bind=self.conn.engine)
