from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, db

app = FastAPI()

# Dependency
def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/customers/", response_model=list[schemas.CustomerOut])
def read_customers(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):
    customers = crud.get_customers(database, skip=skip, limit=limit)
    return customers