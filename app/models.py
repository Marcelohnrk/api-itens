from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Item(Base):
    __tablename__ = "itens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=False, default=1)
    comprado = Column(Boolean, nullable=False, default=False)