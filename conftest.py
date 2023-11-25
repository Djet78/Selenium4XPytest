import pytest
from browsers_config.chrome import chrome_options
from browsers_config.firefox import firefox_options
from browsers_config.edge import edge_options

@pytest.fixture()
def selenium(selenium):
    selenium.maximize_window()
    return selenium
