from fastapi import FastAPI
from bd.database import Base, engine

from routers.genero import router as genero_router
from routers.pelicula import router as pelicula_router
from routers.cliente import router as cliente_router
from routers.empleado import router as empleado_router
from routers.alquiler import router as alquiler_router

app = FastAPI(title="API Alquiler de Películas")

Base.metadata.create_all(bind=engine)

app.include_router(genero_router)
app.include_router(pelicula_router)
app.include_router(cliente_router)
app.include_router(empleado_router)
app.include_router(alquiler_router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}
