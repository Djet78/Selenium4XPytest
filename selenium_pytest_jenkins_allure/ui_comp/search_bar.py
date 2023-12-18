from selenium.webdriver.common.keys import Keys

from submodules.wd_actions import WDActions


class SearchBarComponent(WDActions):
    FIELD_SELECTOR = '//div[@id="search-input"]/input'

    def is_loaded(self) -> bool:
        return self.is_visible(self.FIELD_SELECTOR, timeout=2)

    def search(self, text: str) -> None:
        self.is_loaded()
        self.click(self.FIELD_SELECTOR) \
            .input_text(self.FIELD_SELECTOR, text) \
            .input_text(self.FIELD_SELECTOR, Keys.ENTER)

    def verify_text_in_field(self, expected_text: str) -> None:
        self.is_loaded()
        assert expected_text == self.get_text(
            self.FIELD_SELECTOR
        ), f'Value in search input should be: "{expected_text}"'
