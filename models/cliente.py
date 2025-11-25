from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from datetime import datetime
from bd.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(Text)
    fecha_registro = Column(DateTime, default=datetime.now)
    activo = Column(Boolean, default=True)
