from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    secret_key: str
    access_token_expire_minutes: int = 30
    refresh_token_expire_minutes: int = 60 * 24 * 30
    media_root: str = "/var/app/media"
    static_root: str = "/var/app/static"
    default_currency: str = "ARS"
    default_locale: str = "es-AR"
    default_tz: str = "America/Argentina/Buenos_Aires"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
