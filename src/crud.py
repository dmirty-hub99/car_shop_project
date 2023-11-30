from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Request

from src import schemas, models


def add_brand(db: Session, brand: schemas.BrandSchemas):
    brand_db = models.BrandModel(title=brand.title.upper())
    try:
        db.add(brand_db)
        db.commit()
        db.refresh(brand_db)
        return brand_db
    except IntegrityError:
        raise HTTPException(detail='brand already in db', status_code=402)


def add_car_body(db: Session, car_body: schemas.CarBodySchemas):
    car_body_db = models.CarBodyModel(title=car_body.title.lower())
    try:
        db.add(car_body_db)
        db.commit()
        db.refresh(car_body_db)
        return car_body_db
    except IntegrityError:
        raise HTTPException(detail='car_body already in db', status_code=402)


def add_car(db: Session, car: schemas.CarSchemas):
    car_db = models.CarModel(title=car.title.lower(), brand_id=car.brand_id, year_of_release=car.year_of_release,
                             car_body_id=car.car_body_id, color=car.color)
    db.add(car_db)
    db.commit()
    db.refresh(car_db)
    return car_db


def show_all_cars(db: Session, skip: int, limit: int):
    all_cars = db.scalars(select(models.CarModel).offset(skip).limit(limit)).all()
    if all_cars:
        return all_cars
    raise HTTPException(detail='not cars for your request', status_code=402)


def test(db: Session, request: Request):
    pass
