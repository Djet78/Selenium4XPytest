import allure
import pytest

from api_comp import Booking


@allure.tag('booking', 'api')
@allure.label("owner", "Viacheslav Uslistyi")
@pytest.mark.api
class TestBooking:

    @pytest.mark.parametrize(('book_data', 'expected_code'), [
        ({}, 200),
        ({'firstname': ''}, 200),
        ({'firstname': 100}, 500),
    ])
    def test_book_creation(self, book_data: dict, expected_code: int):
        book = Booking(**book_data)
        resp = book.create()

        assert resp.status_code == expected_code
        if 200 < resp.status_code < 300:
            resp_json = resp.json()
            book.check_properties_type()
            assert resp_json['bookingid']
            assert resp_json['booking'] == book.as_dict()
