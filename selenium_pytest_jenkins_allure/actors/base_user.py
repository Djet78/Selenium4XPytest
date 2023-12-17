import allure
from typing import Self

from selenium.webdriver.remote.webdriver import WebDriver

from selenium_pytest_jenkins_allure.ui_comp import SearchBarComponent, CookiesModalComponent, VideoSearchListComponent


class BaseUser:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('User navigates to main page')
    def navigate_to_main_page(self) -> Self:
        self.driver.get('https://www.youtube.com/')
        return self

    @allure.step('User accept all cookies')
    def accept_all_cookies(self) -> Self:
        cookies_modal = CookiesModalComponent(self.driver)
        cookies_modal.accept_all_cookies()
        return self

    @allure.step('User fill search input with {search_term} and press ENTER')
    def search_video(self, search_term) -> Self:
        search_bar = SearchBarComponent(self.driver)
        search_bar.search(search_term)
        return Self

    @allure.step('User sees the {search_term} in 1st video name')
    def verify_1st_video_contains_term(self, search_term) -> Self:
        video_list = VideoSearchListComponent(self.driver)
        videos = video_list.get_video_list()
        assert search_term.lower() in videos[0].name.lower(), \
            f'Video name "{videos[0].name.lower()}" not contains the search term: "{search_term}"'
        return Self

    @allure.step('User sees the {search_term} in search input')
    def verify_search_input_equals(self, search_term) -> Self:
        search_bar = SearchBarComponent(self.driver)
        search_bar.verify_text_in_field(search_term)
        return Self
