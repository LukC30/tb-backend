from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class MembroUnidade(Base):
    __tablename__ = "tbl_membro_unidade"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    membro_id: Mapped[int] = mapped_column(ForeignKey("tbl_membro.id", ondelete="CASCADE"))
    unidade_id: Mapped[int] = mapped_column(ForeignKey("tbl_unidade.id", ondelete="CASCADE"))

    data_regente: Mapped[int] = mapped_column(Integer) 

    membro: Mapped["Membro"] = relationship(back_populates="assoc_unidade")
    unidade: Mapped["Unidade"] = relationship(back_populates="assoc_membro")

class Unidade(Base):
    __tablename__ = "tbl_unidade"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))

    assoc_membro: Mapped[list["MembroUnidade"]] = relationship(back_populates="unidade")
    def __repr__(self):
        return f"<Unidade(nome={self.nome})>"