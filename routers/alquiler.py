from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from models.alquiler import Alquiler
from models.cliente import Cliente
from models.pelicula import Pelicula
from models.empleado import Empleado
from schemas import Alquiler, AlquilerCreate, AlquilerDevolucion
from datetime import date

router = APIRouter(
    prefix="/alquileres",
    tags=["Alquileres"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Alquiler)
def crear_alquiler(data: AlquilerCreate, db: Session = Depends(get_db)):
    # Validar cliente
    if not db.query(Cliente).filter(Cliente.id == data.cliente_id).first():
        raise HTTPException(400, "Cliente no existe")

    # Validar película
    peli = db.query(Pelicula).filter(Pelicula.id == data.pelicula_id).first()
    if not peli:
        raise HTTPException(400, "Película no existe")

    if peli.copias_disponibles <= 0:
        raise HTTPException(400, "No hay copias disponibles")

    # Validar empleado
    if not db.query(Empleado).filter(Empleado.id == data.empleado_id).first():
        raise HTTPException(400, "Empleado no existe")

    nuevo = Alquiler(
        cliente_id=data.cliente_id,
        pelicula_id=data.pelicula_id,
        empleado_id=data.empleado_id,
        fecha_alquiler=data.fecha_alquiler,
        fecha_devolucion_esperada=data.fecha_devolucion_esperada,
        estado="Activo",
        monto_total=peli.precio_alquiler,
    )

    peli.copias_disponibles -= 1

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[Alquiler])
def listar_alquileres(db: Session = Depends(get_db)):
    return db.query(Alquiler).all()


@router.get("/{alquiler_id}", response_model=Alquiler)
def obtener_alquiler(alquiler_id: int, db: Session = Depends(get_db)):
    alq = db.query(Alquiler).filter(Alquiler.id == alquiler_id).first()
    if not alq:
        raise HTTPException(404, "Alquiler no encontrado")
    return alq


@router.post("/{alquiler_id}/devolver", response_model=Alquiler)
def devolver_pelicula(alquiler_id: int, data: AlquilerDevolucion, db: Session = Depends(get_db)):
    alq = db.query(Alquiler).filter(Alquiler.id == alquiler_id).first()
    if not alq:
        raise HTTPException(404, "Alquiler no encontrado")

    if alq.estado != "Activo":
        raise HTTPException(400, "El alquiler ya fue devuelto")

    alq.fecha_devolucion_real = data.fecha_devolucion_real
    alq.estado = "Devuelto"

    # devolver copia
    peli = db.query(Pelicula).filter(Pelicula.id == alq.pelicula_id).first()
    peli.copias_disponibles += 1

    db.commit()
    db.refresh(alq)
    return alq
