import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        choices=[
            'chrome',
            'firefox',
            'edge',
        ],
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
        choices=[
            'dev',
            'test',
            'stage',
            'prod',
        ],
        help="""
        Specify test environment for further utilization in test. Available options:
         -- dev (default)
         -- test
         -- stage
         -- prod
         """
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):  # noqa: ARG001
    # Get screenshot of a failed test
    result = yield
    result = result.get_result()
    driver = item.funcargs.get('selenium')
    if result.failed and driver:
        allure.attach(driver.get_screenshot_as_png(), "UI Screenshot", attachment_type=AttachmentType.PNG)
