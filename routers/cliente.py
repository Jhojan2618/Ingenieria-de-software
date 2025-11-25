from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from models.cliente import Cliente as ClienteModel
from schemas import Cliente, ClienteCreate, ClienteUpdate

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Cliente)
def crear_cliente(data: ClienteCreate, db: Session = Depends(get_db)):
    nuevo = ClienteModel(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(ClienteModel).all()


@router.get("/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cli = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cli:
        raise HTTPException(404, "Cliente no encontrado")
    return cli


@router.put("/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, datos: ClienteUpdate, db: Session = Depends(get_db)):
    cli = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cli:
        raise HTTPException(404, "Cliente no encontrado")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(cli, key, value)

    db.commit()
    db.refresh(cli)
    return cli


@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cli = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if not cli:
        raise HTTPException(404, "Cliente no encontrado")

    db.delete(cli)
    db.commit()
    return {"mensaje": "Cliente eliminado correctamente"}
