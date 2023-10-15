import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "employee_management_dev")
DB_ADRESS = os.getenv("DB_ADRESS", "localhost:5433")
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADRESS}/{DB_NAME}"

ALEMBIC_INI = "alembic.ini"
MIGRATIONS_PATH = "app/migrations"
