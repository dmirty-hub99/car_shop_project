from pydantic import BaseModel, Field


class BrandSchemas(BaseModel):
    title: str = Field(max_length=30)


class CarBodySchemas(BaseModel):
    title: str = Field(max_length=30)


class CarSchemas(BaseModel):
    title: str = Field(max_length=30)
    brand: BrandSchemas
    year_of_release: int = Field(gt=1999, lt=2025)
    car_body: CarBodySchemas
    color: str = Field(max_length=12)
