from pydantic import BaseSettings

class Settings(BaseSettings):
    token: str
    finder_url: str = 'localhost'
settings = Settings()