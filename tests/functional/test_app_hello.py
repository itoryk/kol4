import datetime

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages.abstract import PageObject
from tests.functional.pages.hello import HelloPage
from tests.functional.utils import screenshot_on_failure
from tests.functional.utils import validate_redirect

url = "http://localhost:8000/h/"


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request):
    page = HelloPage(browser, url)

    assert page.greeting.text == "Hello  {name_header}"
    assert page.address.text == "You are in nowhere"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("bro")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello  {name_header}"
    assert page.address.text == "You are in nowhere"
    assert page.name_input.get_attribute("value") == "bro"

    page.name_input.clear()
    page.address_input.clear()
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello  {name_header}"
    assert page.address.text == "You are in localhost"
    assert page.address_input.get_attribute("value") == "localhost"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("bro")
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello {name_header}"
    assert page.address.text == "You are in localhost"
    assert page.name_input.get_attribute("value") == "bro"
    assert page.address_input.get_attribute("value") == "localhost"


def screenshot_on_failure(test):
    @wraps(test)
    def decorated_test(browser, request, ARTIFACTS_DIR, *args, **kwargs):
        try:
            test(browser, request, *args, **kwargs)
        except Exception:
            ts = datetime.now().strftime(f"%Y.%m.%d.%H.%M.%S")
            test_name = f"{request.module.__name__}.{test.__name__}"
            png = f"{test_name}.{ts}.png"
            html = f"{test_name}.{ts}.html"
            png_path = (ARTIFACTS_DIR / png).resolve()
            html_path = (ARTIFACTS_DIR / html).resolve()
            with html_path.open("w") as _dst:
                _dst.write(browser.page_source)
            browser.save_screenshot(png_path.as_posix())
            raise

    return decorated_test


def validate_redirect(page: PageObject, url: str):
    try:
        redirected = WebDriverWait(page.browser, 4).until(
            expected_conditions.url_matches(url)
        )
        assert redirected
    except TimeoutException as err:
        raise AssertionError("no redirect") from err
