import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = 'Learn FastAPI'
    PROJECT_VERSION: str = '0.1.1'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL = f"""
    postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}
    """.strip()
    TEST_SQLITE_DB: str = os.getenv('TEST_SQLITE_DB')

    ACCESS_TOKEN_EXPIRES_MINUTES: int = 15
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = 'HS256'

    TEST_USER_EMAIL: str = 'test@example.com'


settings = Settings()
