from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from models.pelicula import Pelicula
from models.genero import Genero
from schemas import Pelicula, PeliculaCreate, PeliculaUpdate

router = APIRouter(
    prefix="/peliculas",
    tags=["Películas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Pelicula)
def crear_pelicula(data: PeliculaCreate, db: Session = Depends(get_db)):
    if not db.query(Genero).filter(Genero.id == data.genero_id).first():
        raise HTTPException(400, "El género no existe")

    nueva = Pelicula(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.get("/", response_model=list[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(Pelicula).all()


@router.get("/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    peli = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if not peli:
        raise HTTPException(404, "Película no encontrada")
    return peli


@router.put("/{pelicula_id}", response_model=Pelicula)
def actualizar_pelicula(pelicula_id: int, datos: PeliculaUpdate, db: Session = Depends(get_db)):
    peli = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if not peli:
        raise HTTPException(404, "Película no encontrada")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(peli, key, value)

    db.commit()
    db.refresh(peli)
    return peli


@router.delete("/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    peli = db.query(Pelicula).filter(Pelicula.id == pelicula_id).first()
    if not peli:
        raise HTTPException(404, "Película no encontrada")

    db.delete(peli)
    db.commit()
    return {"mensaje": "Película eliminada correctamente"}
