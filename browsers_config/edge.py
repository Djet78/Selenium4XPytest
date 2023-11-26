import allure
import pytest


@allure.title("Configure Edge browser")
@pytest.fixture
def edge_options(edge_options):
    # edge_options.binary_location = '/path/to/chrome'
    # edge_options.add_extension('/path/to/extension.crx')
    edge_options.page_load_strategy = 'normal'
    edge_options.add_argument("--lang=en")
    # edge_options.add_argument('--kiosk')

    # optimization opts
    edge_options.add_argument('--no-sandbox')
    # edge_options.add_argument('--headless')
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--log-level=3')
    edge_options.add_argument('--default-shm-size=32m')
    edge_options.add_argument('--disable-translate')
    edge_options.add_argument('--disable-extensions')
    # edge_options.add_argument("--proxy-server='direct://'")
    # edge_options.add_argument("--proxy-bypass-list=*")
    edge_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

    return edge_options
