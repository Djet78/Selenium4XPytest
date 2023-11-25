from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

    return Chrome(options=options)
