import allure
import pytest


@allure.tag('searchbar', 'ui')
@allure.label('owner', 'Viacheslav Uslistyi')
@pytest.mark.ui
class TestSearchBar:
    @pytest.mark.parametrize("search_term", ["Test", "vIoLin"])
    @allure.title("Test video search. (Input: {search_term})")
    @allure.description("Verification that search request present in the 1st shown video name.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.link("https://www.youtube.com/", name="Homepage")
    # @allure.testcase("TMS-456")
    def test_video_search(self, unassigned_web_user, search_term):
        unassigned_web_user.navigate_to_main_page() \
            .accept_all_cookies() \
            .search_video(search_term)
        unassigned_web_user.verify_1st_video_contains_term(search_term)

    # @allure.title("Test Authentication")
    @allure.description("Verification that search terms remains in input after a search.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://www.youtube.com/", name="Homepage")
    # @allure.testcase("TMS-456")
    def test_search_value_remains_in_input(self, unassigned_web_user):
        unassigned_web_user.navigate_to_main_page() \
            .accept_all_cookies() \
            .search_video('Test')
        unassigned_web_user.verify_search_input_equals('Test')
