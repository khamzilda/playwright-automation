from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def desktop_app(get_playwright):
    app = App(get_playwright, base_url='https://data.fundraiseup.com/qa-test-7R58U3')
    app.goto('/')
    yield app
    app.close()