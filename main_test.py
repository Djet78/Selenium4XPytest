import allure

from ui_comp import SearchBarComponent, CoockiesModalComponent, VideoSearchListComponent


# @allure.title("Test Authentication")
@allure.description("Verification that search request present in the 1st shown video name.")
@allure.tag("Searchbar")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Viacheslav Uslistyi")
@allure.label("task", "SOME_ID_1")
# @allure.link("https://dev.example.com/", name="Website")
# @allure.testcase("TMS-456")
def test_video_search(selenium):
    selenium.get('https://www.youtube.com/')
    coockies_modal = CoockiesModalComponent(selenium)
    search_bar = SearchBarComponent(selenium)

    coockies_modal.accept_all_coockies()
    search_bar.search('Test')

    video_list = VideoSearchListComponent(selenium)
    videos = video_list.get_video_list()
    assert 'test' in videos[0].name.lower()

# @allure.title("Test Authentication")
@allure.description("Verification that search terms remains in input after a search.")
@allure.tag("Searchbar")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Viacheslav Uslistyi")
@allure.label("task", "SOME_ID_2")
# @allure.link("https://dev.example.com/", name="Website")
# @allure.testcase("TMS-456")
def test_search_value_remains_in_input(selenium):
    selenium.get('https://www.youtube.com/')
    coockies_modal = CoockiesModalComponent(selenium)
    search_bar = SearchBarComponent(selenium)

    coockies_modal.accept_all_coockies()
    search_bar.search('Test')
    search_bar.verify_text_in_field('Test')
