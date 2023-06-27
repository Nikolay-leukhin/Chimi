import os
from dataclasses import dataclass
from dotenv import load_dotenv
from project_config.db_config import DatabaseConfig

load_dotenv()


@dataclass
class Config:
    db: DatabaseConfig


def load_config() -> Config:
    return Config(
        db=DatabaseConfig(
            NAME=os.environ.get('DB_NAME'),
            HOST=os.environ.get('DB_HOST'),
            PORT=os.environ.get('DB_PORT'),
            PASSWORD=os.environ.get('DB_PASSWORD'),
            USER=os.environ.get('DB_USER'),
        )
    )
