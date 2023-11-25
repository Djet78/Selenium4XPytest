import pytest


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/path/to/chrome'
    # chrome_options.add_extension('/path/to/extension.crx')

    chrome_options.page_load_strategy = 'normal'
    chrome_options.add_argument("--lang=en")
    # chrome_options.add_argument('--kiosk')

    # optimization opts
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--default-shm-size=32m')
    chrome_options.add_argument('--disable-translate')
    chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument("--proxy-server='direct://'")
    # chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

    return chrome_options
