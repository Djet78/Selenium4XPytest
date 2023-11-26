import allure
import pytest

from pytest_hooks import *
from actors import UnassignedUser
from browsers_config.chrome import chrome_options
from browsers_config.firefox import firefox_options
from browsers_config.edge import edge_options


@allure.title('Launch webdriver')
@pytest.fixture()
def selenium(selenium):
    selenium.set_window_size(1920, 1080)
    yield selenium


@allure.title('Create Unassigned user')
@pytest.fixture()
def unassigned_user(selenium):
    return UnassignedUser(selenium)
