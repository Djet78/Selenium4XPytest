from typing import Self
from selenium.webdriver.common.keys import Keys

from ui_comp import BaseComp


class SearchBarComponent(BaseComp):
    FIELD_SELECTOR = '//div[@id="search-input"]/input'

    def is_loaded(self) -> bool:
        return self._is_visible(self.FIELD_SELECTOR, timeout=2)

    def search(self, text: str) -> None:
        self.is_loaded()
        self._click(self.FIELD_SELECTOR) \
            ._input_text(self.FIELD_SELECTOR, text) \
            ._input_text(self.FIELD_SELECTOR, Keys.ENTER)

    def verify_text_in_field(self, expected_text: str) -> None:
        self.is_loaded()
        assert expected_text == self._get_text(self.FIELD_SELECTOR), \
            f'Value in search input should be: "{expected_text}"'
