from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL_BANCO = "sqlite:///./itens.db"

engine = create_engine(URL_BANCO, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()