import allure
import pytest

from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):
    result = yield
    result = result.get_result()
    driver = item.funcargs.get('selenium')
    if result.failed and driver:
        allure.attach(driver.get_screenshot_as_png(), "UI Screenshot", attachment_type=AttachmentType.PNG)


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
         """,
    )
