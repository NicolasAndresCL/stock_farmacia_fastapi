from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Stock Farmacia FastAPI")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/medicamentos/", response_model=list[schemas.Medicamento])
def leer_medicamentos(db: Session = Depends(get_db)):
    return crud.get_medicamentos(db)

@app.post("/medicamentos/", response_model=schemas.Medicamento)
def crear_medicamento(medicamento: schemas.MedicamentoCreate, db: Session = Depends(get_db)):
    return crud.create_medicamento(db, medicamento)
