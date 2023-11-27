import allure
import pytest

from selenium.webdriver import Chrome, Firefox, Edge

from pytest_hooks import *
from actors import UnassignedUser
from browsers_config.chrome import chrome_options
from browsers_config.firefox import firefox_options
from browsers_config.edge import edge_options


@allure.title('Launch webdriver')
@pytest.fixture(scope='session')
def selenium(request):
    opt = request.config.getoption("--driver")
    opt_map = {
        'chrome': (Chrome, chrome_options()),
        'edge': (Edge, edge_options()),
        'firefox': (Firefox, firefox_options()),
    }
    webdriver, options = opt_map[opt][0], opt_map[opt][1]
    selenium = webdriver(options)
    selenium.set_window_size(1920, 1080)

    yield selenium

    selenium.close()


@allure.title('Create Unassigned user')
@pytest.fixture()
def unassigned_user(selenium):
    return UnassignedUser(selenium)
