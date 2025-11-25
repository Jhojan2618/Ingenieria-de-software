from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

#GÉNEROS

class GeneroBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class GeneroCreate(GeneroBase):
    pass

class Genero(GeneroBase):
    id: int

    class Config:
        from_attributes = True


#PELÍCULAS

class PeliculaBase(BaseModel):
    titulo: str
    descripcion: Optional[str]
    anio_lanzamiento: int
    duracion_minutos: int
    genero_id: int
    precio_alquiler: float
    copias_disponibles: int = 1

class PeliculaCreate(PeliculaBase):
    pass

class PeliculaUpdate(BaseModel):
    titulo: Optional[str]
    descripcion: Optional[str]
    anio_lanzamiento: Optional[int]
    duracion_minutos: Optional[int]
    genero_id: Optional[int]
    precio_alquiler: Optional[float]
    copias_disponibles: Optional[int]

class Pelicula(PeliculaBase):
    id: int

    class Config:
        from_attributes = True


#CLIENTES


class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: str
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]
    direccion: Optional[str]
    
from datetime import datetime

class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime
    activo: bool

    class Config:
        from_attributes = True  # antes llamado orm_mode = True

#EMPLEADOS

class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: str
    cargo: str

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    email: Optional[EmailStr]
    telefono: Optional[str]
    cargo: Optional[str]

class Empleado(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr
    telefono: str
    cargo: str
    fecha_contratacion: datetime
    activo: bool

    class Config:
        from_attributes = True

#ALQUILERES

class AlquilerBase(BaseModel):
    cliente_id: int
    pelicula_id: int
    empleado_id: int
    fecha_alquiler: date
    fecha_devolucion_esperada: date

class AlquilerCreate(AlquilerBase):
    pass

class AlquilerDevolucion(BaseModel):
    fecha_devolucion_real: date

class Alquiler(BaseModel):
    id: int
    cliente_id: int
    pelicula_id: int
    empleado_id: int
    fecha_alquiler: date
    fecha_devolucion_esperada: date
    fecha_devolucion_real: Optional[date]
    estado: str
    monto_total: float

    class Config:
        from_attributes = True