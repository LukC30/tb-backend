import enum
from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from datetime import date

class Login(Base):
    __tablename__ = "tbl_login"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    senha: Mapped[str] = mapped_column(String(200))

    id_user: Mapped[int] = mapped_column(ForeignKey("tbl_membro.id"))
    membro: Mapped["Membro"] = relationship(back_populates="login")

    def __repr__(self):
        return f"<Login=(email={self.email}, nome_membro={self.membro.nome})>"