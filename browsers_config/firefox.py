import pytest


@pytest.fixture
def firefox_options(firefox_options):
    # firefox_options.binary_location = '/path/to/chrome'
    # firefox_options.add_extension('/path/to/extension.crx')
    firefox_options.page_load_strategy = 'normal'
    # firefox_options.add_argument('-headless')
    firefox_options.set_preference("intl.accept_languages", 'en-us')
    firefox_options.set_preference("dom.disable_beforeunload", True)
    return firefox_options
