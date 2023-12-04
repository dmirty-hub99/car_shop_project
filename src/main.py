from fastapi import Depends, FastAPI, Request
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal
from .dependencies import all_car_parameters

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/add_brand', response_model=schemas.BrandSchemas)
def add_brand(brand: schemas.BrandSchemas, db: Session = Depends(get_db)):
    return crud.add_brand(brand=brand, db=db)


@app.post('/add_car_body', response_model=schemas.CarBodySchemas)
def add_car_body(car_body: schemas.CarBodySchemas, db: Session = Depends(get_db)):
    return crud.add_car_body(car_body=car_body, db=db)


@app.post('/add_car', response_model=schemas.CarSchemas)
def add_car(car: schemas.CarSchemas, db: Session = Depends(get_db)):
    return crud.add_car(car=car, db=db)


@app.get('/show_all_cars', response_model=list[schemas.CarSchemas], dependencies=[Depends(all_car_parameters)])
def show_all_cars(request: Request, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.show_all_cars(request, db, skip, limit)


@app.delete('/delete_car/{car_id}')
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return crud.delete_car(car_id, db)


@app.get('/test')
def test(request: Request, db: Session = Depends(get_db)):
    return crud.test(db, request)
