from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from models.genero import Genero
from models.pelicula import Pelicula
from schemas import Genero, GeneroCreate

router = APIRouter(
    prefix="/generos",
    tags=["Géneros"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Genero)
def crear_genero(genero: GeneroCreate, db: Session = Depends(get_db)):
    nuevo = Genero(**genero.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[Genero])
def listar_generos(db: Session = Depends(get_db)):
    return db.query(Genero).all()


@router.get("/{genero_id}", response_model=Genero)
def obtener_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if not genero:
        raise HTTPException(404, "Género no encontrado")
    return genero


@router.put("/{genero_id}", response_model=Genero)
def actualizar_genero(genero_id: int, datos: GeneroCreate, db: Session = Depends(get_db)):
    genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if not genero:
        raise HTTPException(404, "Género no encontrado")

    for key, value in datos.dict().items():
        setattr(genero, key, value)

    db.commit()
    db.refresh(genero)
    return genero


@router.delete("/{genero_id}")
def eliminar_genero(genero_id: int, db: Session = Depends(get_db)):
    genero = db.query(Genero).filter(Genero.id == genero_id).first()
    if not genero:
        raise HTTPException(404, "Género no encontrado")

    peliculas_asociadas = db.query(Pelicula).filter(Pelicula.genero_id == genero_id).count()
    if peliculas_asociadas > 0:
        raise HTTPException(400, "No se puede eliminar: el género tiene películas asociadas")

    db.delete(genero)
    db.commit()

    return {"mensaje": "Género eliminado correctamente"}
