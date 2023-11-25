from time import sleep

from ui_comp import SearchBarComponent, CoockiesModalComponent, VideoSearchListComponent


def test_video_search(selenium):
    with selenium as driver:
        driver.get('https://www.youtube.com/')
        coockies_modal = CoockiesModalComponent(driver)
        search_bar = SearchBarComponent(driver)

        coockies_modal.accept_all_coockies()
        sleep(5)
        search_bar.search('Test')
        sleep(5)

        video_list = VideoSearchListComponent(driver)
        videos = video_list.get_video_list()
        assert 'test' in videos[0].name.lower()
