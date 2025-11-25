from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from bd.database import Base

class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    cargo = Column(String(50), nullable=False)
    fecha_contratacion = Column(DateTime, default=datetime.now)
    activo = Column(Boolean, default=True)
