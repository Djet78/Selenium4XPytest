from time import sleep

from ui_comp import SearchBarComponent, CoockiesModalComponent, VideoSearchListComponent


def test_video_search(selenium):
    selenium.get('https://www.youtube.com/')
    coockies_modal = CoockiesModalComponent(selenium)
    search_bar = SearchBarComponent(selenium)

    coockies_modal.accept_all_coockies()
    search_bar.search('Test')

    video_list = VideoSearchListComponent(selenium)
    videos = video_list.get_video_list()
    assert 'test' in videos[0].name.lower()


def test_search_value_remains_in_input(selenium):
    selenium.get('https://www.youtube.com/')
    coockies_modal = CoockiesModalComponent(selenium)
    search_bar = SearchBarComponent(selenium)

    coockies_modal.accept_all_coockies()
    search_bar.search('Test')
    search_bar.verify_text_in_field('Test')
