from pydantic import BaseSettings

class Settings(BaseSettings):
    token: str = "1180719509:AAHGQvu8mVcNLwWMSBNj9OsGi87OR5EC83g"
    finder_url: str = 'localhost'
settings = Settings()