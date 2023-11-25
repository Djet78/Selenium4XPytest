from time import sleep

from browsers_config.chrome import get_chrome_driver
from ui_comp import SearchBarComponent, CoockiesModalComponent, VideoSearchListComponent


with get_chrome_driver() as driver:
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
