from pydantic import BaseSettings, PostgresDsn, validator

class AppSettings(BaseSettings):
  DB_SERVER: str
  DB_USER: str
  DB_PASSWORD: str
  DB_NAME: str
  SQLALCHEMY_DATABASE_URI: PostgresDsn|None

  @validator("SQLALCHEMY_DATABASE_URI", pre=True)
  def assemble_db_connection(cls, v: str|None, values: dict[str, any]):
    if isinstance(v, str):
      return v
    return PostgresDsn.build(
        scheme="postgresql",
        user=values.get("DB_USER"),
        password=values.get("DB_PASSWORD"),
        host=values.get("DB_SERVER"),
        path=f"/{values.get('DB_NAME') or ''}",
    )

  class Config:
    env_file = ".env"


appsettings = AppSettings()