import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models, schemas
from src.crud import add_car
from src.database import engine


@pytest.fixture()
def delete_test_brand():
    with Session(engine) as db:
        test_brand = db.scalars(select(models.BrandModel).where(models.BrandModel.title == 'TEST_BRAND')).first()
        if test_brand:
            db.delete(test_brand)
            db.commit()


@pytest.fixture()
def delete_test_car_body():
    with Session(engine) as db:
        test_car_body = db.scalars(
            select(models.CarBodyModel).where(models.CarBodyModel.title == 'test_car_body')).first()
        if test_car_body:
            db.delete(test_car_body)
            db.commit()


@pytest.fixture()
def delete_all_test_cars():
    with Session(engine) as db:
        test_cars = db.scalars(select(models.CarModel).where(models.CarModel.title == 'test_car')).all()
        if test_cars:
            for car in test_cars:
                db.delete(car)
            db.commit()


@pytest.fixture()
def create_car_for_delete():
    with Session(engine) as db:
        delete_car = db.scalars(select(models.CarModel).where(models.CarModel.title == 'test_delete_car')).first()
        if not delete_car:
            add_car(db, schemas.CarSchemas(title='test_delete_car', brand=schemas.BrandSchemas(title='bmw'),
                                           year_of_release=2010, car_body=schemas.CarBodySchemas(title='sedan'),
                                           color='red'))
        delete_car: models.CarModel = db.scalars(
            select(models.CarModel).where(models.CarModel.title == 'test_delete_car')).first()
    return delete_car.id
