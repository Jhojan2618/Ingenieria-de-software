from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from bd.database import Base

class Pelicula(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text)
    anio_lanzamiento = Column(Integer)
    duracion_minutos = Column(Integer)
    genero_id = Column(Integer, ForeignKey("generos.id"))
    precio_alquiler = Column(Float, nullable=False)
    copias_disponibles = Column(Integer, default=1)

    genero = relationship("Genero")
