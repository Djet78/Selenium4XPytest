from selenium.webdriver.firefox.options import Options


def firefox_options() -> Options:
    opt = Options()
    # opt.binary_location = '/path/to/chrome'
    # opt.add_extension('/path/to/extension.crx')
    opt.page_load_strategy = 'normal'
    # opt.add_argument('-headless')
    opt.set_preference("intl.accept_languages", 'en-us')
    opt.set_preference("dom.disable_beforeunload", True)
    return opt
