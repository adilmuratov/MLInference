from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Request(Base):
    model_name: Mapped[str] = mapped_column(
        String,
        default=""
    )
    text: Mapped[str] = mapped_column(
        Text, 
        default=""
    )
    answer: Mapped[bool] = mapped_column(
        Boolean, 
        default=True
    )