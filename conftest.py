import allure
import pytest

from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.remote.webdriver import WebDriver

from actors import UnassignedUser
from browsers_config import chrome_options, edge_options, firefox_options
from pytest_hooks import *
from utils import add_pytest_res_evn_file


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
    selenium: WebDriver = webdriver(options)
    selenium.set_window_size(1920, 1080)

    add_pytest_res_evn_file(request.config, 'DRIVER', selenium.capabilities['browserName'])
    add_pytest_res_evn_file(request.config, 'BROWSER_VERSION', selenium.capabilities['browserVersion'])
    add_pytest_res_evn_file(request.config, 'OS', selenium.capabilities['platformName'])
    add_pytest_res_evn_file(request.config, 'ENVIRONMENT', request.config.getoption('--env'))
    # add_pytest_res_evn_file(request.config, 'BROWSER_RESOLUTION', selenium.get_window_size())

    yield selenium

    selenium.close()


@allure.title('Create Unassigned user')
@pytest.fixture()
def unassigned_web_user(selenium):
    return UnassignedUser(selenium)
