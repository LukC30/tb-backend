import enum
from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import date

class CargoMembro(enum.Enum):
    CONSELHEIRO = "Conselheiro"
    CAPITAO = "Capitão"
    SECRETARIO = "Secretário"
    TESOUREIRO = "Tesoureiro"
    DESBRAVADOR = "Desbravador"

class Membro(Base):
    __tablename__ = "tbl_membro"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    nome: Mapped[str] = mapped_column(String(100))
    cargo: Mapped[CargoMembro] = mapped_column(Enum(CargoMembro))
    data_nascimento: Mapped[date] = mapped_column(date)
    telefone: Mapped[str] = mapped_column(String(11), unique=True)

    login: Mapped["Login"] = relationship(back_populates='membro')
    def __repr__(self) -> str:
            return f"<Membro(nome={self.nome}, cargo={self.cargo})>"