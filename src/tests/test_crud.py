from fastapi.testclient import TestClient

from src.main import app
from src.tests.json_requests import add_car_json

client = TestClient(app)


def test_add_brand(delete_test_brand):
    response = client.post('/add_brand', json={
        "title": "test_brand"})
    assert response.status_code == 200
    assert response.json() == {"title": 'TEST_BRAND'}


def test_add_car_body(delete_test_car_body):
    response = client.post('/add_car_body', json={
        "title": "test_car_body"})
    assert response.status_code == 200
    assert response.json() == {"title": 'test_car_body'}


def test_add_car(delete_all_test_cars):
    response = client.post('/add_car', json=add_car_json)
    assert response.status_code == 200
    assert response.json()['title'] == 'test_car'
    assert response.json()['year_of_release'] == 2000
    assert response.json()['color'] == 'blue'
    assert response.json()['brand']['title'] == 'AUDI'
    assert response.json()['car_body']['title'] == 'sedan'


def test_delete_car(create_car_for_delete):
    delete_car_id = create_car_for_delete
    response = client.delete(f'/delete_car/{delete_car_id}')
    assert response.json() == {"status": "object successfully deleted"}


def test_delete_error_car_id():
    response = client.delete(f'/delete_car/1000000')
    assert response.json() == {"detail": "not object in db"}
