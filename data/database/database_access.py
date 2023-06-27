from data.database.database_connection import DatabaseConnection


class DatabaseAccess:
    def __init__(self, conn: DatabaseConnection):
        self.conn = conn

