from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from submodules.wd_actions import WDActions


class VideoPreviewComponent(WDActions):
    TITLE_DATA_SELECTOR = './/a[@id="video-title"]'

    def __init__(self, driver: WebDriver, element: WebElement):
        super().__init__(driver)
        self.element = element
        self.name = self.get_name()

    def get_name(self) -> str | bool:
        title_data = self.element.find_element(By.XPATH, self.TITLE_DATA_SELECTOR)
        return title_data.get_attribute('title')


class VideoSearchListComponent(WDActions):
    LIST_SELECTOR = '//ytd-search'
    VIDEO_PREVIEW_SELECTOR = '//ytd-video-renderer'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.video_list = self.get_video_list()

    def _is_loaded(self) -> bool:
        return self.is_visible(self.LIST_SELECTOR, timeout=10)

    def get_video_list(self) -> list[VideoPreviewComponent]:
        self._is_loaded()
        previews = []
        for preview in self.find_el(self.VIDEO_PREVIEW_SELECTOR, 3, True):
            previews.append(VideoPreviewComponent(self.driver, preview))
        return previews
