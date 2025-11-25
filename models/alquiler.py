from sqlalchemy import Column, Integer, Date, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from datetime import date
from bd.database import Base

class Alquiler(Base):
    __tablename__ = "alquileres"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    pelicula_id = Column(Integer, ForeignKey("peliculas.id"))
    empleado_id = Column(Integer, ForeignKey("empleados.id"))

    fecha_alquiler = Column(Date, default=date.today)
    fecha_devolucion_esperada = Column(Date)
    fecha_devolucion_real = Column(Date, nullable=True)

    estado = Column(String(20))
    monto_total = Column(Float)

    cliente = relationship("Cliente")
    pelicula = relationship("Pelicula")
    empleado = relationship("Empleado")
