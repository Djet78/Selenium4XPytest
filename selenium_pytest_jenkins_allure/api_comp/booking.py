from dataclasses import dataclass, field

import requests

from submodules.type_validator import BaseDataclass


@dataclass
class Dates(BaseDataclass):
    checkin: str = '2022-01-01'
    checkout: str = '2023-01-01'


@dataclass
class Booking(BaseDataclass):
    firstname: str = 'Test'
    lastname: str = 'Book'
    totalprice: int = 1
    depositpaid: bool = True
    additionalneeds: str = 'No'
    bookingdates: Dates = field(default_factory=Dates)

    def create(self, **kwargs) -> requests.Response:
        self.dict2object(kwargs)
        resp = requests.post('https://restful-booker.herokuapp.com/booking', json=self.as_dict())
        return resp
