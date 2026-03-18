from sqlalchemy import String, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from app.core.database import Base
from .domain import CargoMembro


class Membro(Base):
    __tablename__ = "tbl_membro"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    nome: Mapped[str] = mapped_column(String(100))
    cargo: Mapped[CargoMembro] = mapped_column(Enum(CargoMembro))
    data_nascimento: Mapped[date] = mapped_column(Date)
    telefone: Mapped[str] = mapped_column(String(11), unique=True)

    login: Mapped["Login"] = relationship(back_populates='membro')
    def __repr__(self) -> str:
            return f"<Membro(nome={self.nome}, cargo={self.cargo})>"