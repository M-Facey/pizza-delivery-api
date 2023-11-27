from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import PG_USERNAME, PG_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    F"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{DB_HOST}/{DB_NAME}",
    echo=True
)

Base = declarative_base()
Session = sessionmaker()