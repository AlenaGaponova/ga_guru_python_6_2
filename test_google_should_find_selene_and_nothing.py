from selene import be, have
from selene.support.shared import browser
import pytest


@pytest.fixture()
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1200
    browser.open('https://google.com')


def test_google_should_find_selene(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
