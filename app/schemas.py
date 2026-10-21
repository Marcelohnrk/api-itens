from pydantic import BaseModel, Field


class ItemEntrada(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    quantidade: int = Field(default=1, gt=0)
    comprado: bool = False


class ItemSaida(ItemEntrada):
    id: int