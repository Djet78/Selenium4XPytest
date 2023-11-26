import os

import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="""
        Pytest will run tests against specified browser. Available options:
         -- chrome (default)
         -- firefox
         -- edge
         """
    )
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="""
        Specify test environment for further utilization in test. Available options:
         -- dev (default)
         -- test
         -- stage
         -- prod
         """
    )


@pytest.hookimpl
def pytest_report_collectionfinish(config, start_path, startdir, items):
    alluredir = config.getoption('--alluredir')
    if not os.path.exists(alluredir):
        os.mkdir(alluredir)

    allure_env_path = os.path.join(alluredir, 'environment.properties')
    with open(allure_env_path, 'w') as _f:
        _f.write(f"""
Environment={config.getoption('--env')}
Driver={config.getoption('--driver')}
        """)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):
    result = yield
    result = result.get_result()
    driver = item.funcargs.get('selenium')
    if result.failed and driver:
        allure.attach(driver.get_screenshot_as_png(), "UI Screenshot", attachment_type=AttachmentType.PNG)
