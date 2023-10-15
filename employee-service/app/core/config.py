import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "employee_management_dev")
DB_ADRESS = os.getenv("DB_ADRESS", "employee_management_db")
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADRESS}/{DB_NAME}"

SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 8000
SERVER_LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
SERVER_WORKER_NUMBERS = 1

ENV = os.getenv("ENV", "dev")
PROJECT_NAME = "employee_management"
CORS_ORIGINS = os.getenv("CORS_HOSTS", "http://localhost:8080")
API_KEY = os.getenv("API_KEY")
APP_VERSION = os.getenv("VERSION", "1.0.0")
APP_NAME = "employee-service"