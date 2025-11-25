from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from models.empleado import Empleado
from schemas import Empleado, EmpleadoCreate, EmpleadoUpdate

router = APIRouter(
    prefix="/empleados",
    tags=["Empleados"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Empleado)
def crear_empleado(data: EmpleadoCreate, db: Session = Depends(get_db)):
    nuevo = Empleado(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[Empleado])
def listar_empleados(db: Session = Depends(get_db)):
    return db.query(Empleado).all()


@router.get("/{empleado_id}", response_model=Empleado)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    emp = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not emp:
        raise HTTPException(404, "Empleado no encontrado")
    return emp


@router.put("/{empleado_id}", response_model=Empleado)
def actualizar_empleado(empleado_id: int, datos: EmpleadoUpdate, db: Session = Depends(get_db)):
    emp = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not emp:
        raise HTTPException(404, "Empleado no encontrado")

    for key, value in datos.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int, db: Session = Depends(get_db)):
    emp = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not emp:
        raise HTTPException(404, "Empleado no encontrado")

    db.delete(emp)
    db.commit()
    return {"mensaje": "Empleado eliminado correctamente"}
