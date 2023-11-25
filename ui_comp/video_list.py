from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from ui_comp import BaseComp


class VideoPreviewComponent(BaseComp):
    TITLE_DATA_SELECTOR = f'.//a[@id="video-title"]'

    def __init__(self, driver: WebDriver, element: WebElement):
        super().__init__(driver)
        self.element = element
        self.name = self._get_name()

    def _get_name(self) -> Union[str, bool]:
        title_data = self.element.find_element(By.XPATH, self.TITLE_DATA_SELECTOR)
        return title_data.get_attribute('title')


class VideoSearchListComponent(BaseComp):
    LIST_SELECTOR = '//ytd-search'
    VIDEO_PREVIEW_SELECTOR = '//ytd-video-renderer'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.video_list = self.get_video_list()

    def _is_loaded(self) -> bool:
        return self._is_visible(self.LIST_SELECTOR, timeout=10)

    def get_video_list(self) -> list[VideoPreviewComponent]:
        self._is_loaded()
        previews = []
        for preview in self._find_el(self.VIDEO_PREVIEW_SELECTOR, 3, True):
            previews.append(VideoPreviewComponent(self.driver, preview))
        return previews
