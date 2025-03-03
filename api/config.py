from decouple import config
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = config("POSTGRES_HOST",cast=str, default="backend")
POSTGRES_PORT = config("POSTGRES_PORT", cast=int, default=5432)
POSTGRES_USER = config("POSTGRES_USER", cast=str, default="postgres")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str, default="postgres")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="appdb")