from time import sleep
from typing import Self

from ui_comp import BaseComp


class CookiesModalComponent(BaseComp):
    MODAL_SELECTOR = '//*[@id="dialog"]'
    ACCEPT_ALL_SELECTOR = f'{MODAL_SELECTOR}//yt-button-shape[contains(normalize-space(), "Accept all")]'

    def is_loaded(self) -> bool:
        return self._is_visible(self.MODAL_SELECTOR, 3)

    def accept_all_cookies(self) -> Self:
        self.is_loaded()
        approve_btn = self._find_el(self.ACCEPT_ALL_SELECTOR)
        self._js_scroll_to(self.ACCEPT_ALL_SELECTOR)
        approve_btn.click()
        sleep(3)  # Page reloaded, and I'm lazy to make proper check
        return self
