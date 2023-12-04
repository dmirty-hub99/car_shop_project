from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models
from src.database import engine
from src.main import app

client = TestClient(app)


def test_add_brand():
    response = client.post('/add_brand', json={
        "title": "test_brand"})
    assert response.status_code == 200
    assert response.json() == {"title": 'TEST_BRAND'}


def test_add_car_body():
    response = client.post('/add_car_body', json={
        "title": "test_car_body"})
    assert response.status_code == 200
    assert response.json() == {"title": 'test_car_body'}


def test_default_end():
    with Session(engine) as db:
        test_brand = db.scalars(select(models.BrandModel).where(models.BrandModel.title == 'TEST_BRAND')).first()
        test_car_body = db.scalars(
            select(models.CarBodyModel).where(models.CarBodyModel.title == 'test_car_body')).first()
        try:
            db.delete(test_brand)
            db.delete(test_car_body)
            db.commit()
        except:
            pass
