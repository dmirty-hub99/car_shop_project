from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import schemas, models


def add_brand(db: Session, brand: schemas.BrandSchemas):
    brand_db = models.BrandModel(title=brand.title.upper())
    stmt = select(models.BrandModel).where(models.BrandModel.title == brand_db.title)
    result_stmt = db.execute(stmt).all()

    if not result_stmt:
        db.add(brand_db)
        db.commit()
        db.refresh(brand_db)
        return brand_db

    raise HTTPException(detail='brand already in db', status_code=402)


def add_car_body(db: Session, car_body: schemas.CarBodySchemas):
    car_body_db = models.CarBodyModel(title=car_body.title.lower())
    stmt = select(models.CarBodyModel).where(models.CarBodyModel.title == car_body_db.title)
    result_stmt = db.execute(stmt).all()

    if not result_stmt:
        db.add(car_body_db)
        db.commit()
        db.refresh(car_body_db)
        return car_body_db

    raise HTTPException(detail='car_body already in db', status_code=402)


def add_car(db: Session, car: schemas.CarSchemas):
    car_db = models.CarModel(title=car.title.lower(), brand_id=car.brand_id, year_of_release=car.year_of_release,
                             car_body_id=car.car_body_id, color=car.color)
    db.add(car_db)
    db.commit()
    db.refresh(car_db)
    return car_db


def show_all_cars(db: Session, skip: int = 0, limit: int = 100):
    all_cars = db.scalars(select(models.CarModel).offset(skip).limit(limit)).all()
    return all_cars


def test(db: Session):
    # all_cars = db.scalars(select(models.CarModel)).all()
    #
    # res = select(models.CarModel).where(models.CarModel.brand_id == 2003)
    # all_bmw = db.scalars(select(models.CarModel).where(models.CarModel.brand_id == 1)).all()
    #
    # return all_cars[0].brand.title

    return 'ok'
