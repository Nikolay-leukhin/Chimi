from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    HOST: str
    NAME: str
    PASSWORD: str
    USER: str
    PORT: str