from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ADMIN_ID: int
    base_url: str
    APP_URL: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config_settings = Settings()
