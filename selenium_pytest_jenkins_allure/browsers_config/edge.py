from selenium.webdriver.edge.options import Options


def edge_options() -> Options:
    opt = Options()
    # opt.binary_location = '/path/to/chrome'
    # opt.add_extension('/path/to/extension.crx')
    opt.page_load_strategy = 'normal'
    opt.add_argument('--lang=en')
    # opt.add_argument('--kiosk')

    # optimization opts
    opt.add_argument('--no-sandbox')
    # opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--log-level=3')
    opt.add_argument('--default-shm-size=32m')
    opt.add_argument('--disable-translate')
    opt.add_argument('--disable-extensions')
    # opt.add_argument("--proxy-server='direct://'")
    # opt.add_argument("--proxy-bypass-list=*")
    opt.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
    return opt
