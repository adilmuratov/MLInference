from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

DB_PATH + BASE_DIR / "db.sqlite3"

class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True

class Settings(BaseSettings):
    db: DBSettings = DBSettings()

settings = Settings()