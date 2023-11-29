from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .database import Base


class BrandModel(Base):
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    cars: Mapped[List['CarModel']] = relationship(back_populates='brand')


class CarBodyModel(Base):
    __tablename__ = 'car_bodies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    cars: Mapped[List['CarModel']] = relationship(back_populates='car_body')


class CarModel(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'))
    brand: Mapped['BrandModel'] = relationship(back_populates='cars')
    year_of_release: Mapped[int]
    car_body_id: Mapped[int] = mapped_column(ForeignKey('car_bodies.id'))
    car_body: Mapped['CarBodyModel'] = relationship(back_populates='cars')
    color: Mapped[str]

    def __repr__(self):
        return self.title
