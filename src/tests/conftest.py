import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models
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
