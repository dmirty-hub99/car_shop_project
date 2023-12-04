from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Request
from sqlalchemy.orm.exc import UnmappedInstanceError

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


def show_all_cars(request: Request, db: Session, skip: int, limit: int):
    query = select(models.CarModel).offset(skip).limit(limit)

    if request.query_params:
        for key, value in request.query_params.items():
            try:
                query = query.filter(getattr(models.CarModel, key) == value)
            except AttributeError:
                pass

    # if brand:
    #     query_brand_id = select(models.BrandModel.id).where(models.BrandModel.title == brand.upper())
    #     brand_id = db.scalars(query_brand_id).first()
    #     query = query.filter(models.CarModel.brand_id == brand_id)
    # if car_body:
    #     query = query.filter(getattr(models.CarModel, 'car_body') == car_body.upper())

    all_cars = db.scalars(query).all()
    if all_cars:
        return all_cars
    raise HTTPException(detail='not cars for your request', status_code=404)


def delete_car(car_id, db: Session):
    delete_object = db.get(models.CarModel, car_id)
    try:
        db.delete(delete_object)
        db.commit()
    except UnmappedInstanceError:
        raise HTTPException(detail='not object in db', status_code=402)

    return {"status": "object successfully deleted"}


def test(db: Session, request: Request):
    brand = 'audi'

    query_brand_name = select(models.BrandModel.id).where(models.BrandModel.title == brand.upper())
    brand_name = db.scalars(query_brand_name).first()

    query = select(models.CarModel).where(models.CarModel.brand_id == brand_name)
    all_cars = db.scalars(query).all()

    return all_cars
