from dataclasses import dataclass, field

import requests

from selenium_pytest_jenkins_allure.env_configurator import EnvConfigurator
from submodules.type_validator import BaseDataclass


@dataclass
class BaseEnvDataClass(BaseDataclass):
    def get_env_info(self):
        return EnvConfigurator().env


@dataclass
class Dates(BaseEnvDataClass):
    checkin: str = '2022-01-01'
    checkout: str = '2023-01-01'


@dataclass
class Booking(BaseEnvDataClass):
    firstname: str = 'Test'
    lastname: str = 'Book'
    totalprice: int = 1
    depositpaid: bool = True
    additionalneeds: str = 'No'
    bookingdates: Dates = field(default_factory=Dates)

    def create(self, **kwargs) -> requests.Response:
        self.dict2object(kwargs)
        resp = requests.post('https://restful-booker.herokuapp.com/booking', json=self.as_dict(), timeout=5)
        return resp
