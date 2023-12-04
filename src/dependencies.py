from fastapi import Depends


def all_car_parameters(year_of_release: int | None = None, color: str | None = None, brand_name: str | None = None,
                       car_body_name: str | None = None):
    return {'brand_name': brand_name, 'car_body_name': car_body_name}
