import pytest

from tests.functional.pages.hello import HelloPage
from tests.functional.utils import screenshot_on_failure
from tests.functional.utils import validate_redirect

url = "http://localhost:8000/h/"


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request):
    page = HelloPage(browser, url)

    assert page.greeting.text == "Hello bro"
    assert page.address.text == "You are at nowhere"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("broz")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello broz"
    assert page.address.text == "You are at nowhere"
    assert page.name_input.get_attribute("value") == "bro"

    page.name_input.clear()
    page.address_input.clear()
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello bro"
    assert page.address.text == "You are at localhost"
    assert page.address_input.get_attribute("value") == "localhost"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("bro")
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello bro"
    assert page.address.text == "You are at localhost"
    assert page.name_input.get_attribute("value") == "bro"
    assert page.address_input.get_attribute("value") == "localhost"
