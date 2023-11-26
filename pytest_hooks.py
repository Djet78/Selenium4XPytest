import allure
import pytest

from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(call, item):
    result = yield
    result = result.get_result()
    driver = item.funcargs['selenium']
    if result.failed:
        allure.attach(driver.get_screenshot_as_png(), "UI Screenshot", attachment_type=AttachmentType.PNG)
