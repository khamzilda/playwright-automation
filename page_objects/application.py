from playwright.sync_api import Playwright, expect
import re

class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url


    def goto(self, endpoint: str):
        self.page.goto(self.base_url + endpoint)

    def check_page_start(self):
        return expect(self.page).to_have_title(re.compile("QA Engineer Test"))


    def give_now_button(self):
        self.page.frame_locator("#XBGSFAMB").locator("div[role=\"button\"]:has-text(\"Give Now\")").click()

    def secure_donation(self):
        self.page.wait_for_url(self.base_url + "/?form=FUNCDKBDSGW")
        self.frame_path = self.page.frame_locator("iframe").nth(4)
        self.frame_path.locator("button:has-text(\"Monthly\")").click()
        self.frame_path.locator("input[placeholder=\"Other\"]").fill("100")
        self.frame_path.locator("select[class=\"currency-select-control\"]").select_option("USD")
        self.frame_path.locator("button:has-text(\"Donate monthly\")").click()

    def check_cover_transaction_costs(self):
        cover_transaction_costs = self.frame_path.locator("[id=\"popover-fees\"]")
        return expect(cover_transaction_costs).to_have_attribute("aria-checked", "true")

    def payment_option(self):
        self.frame_path.locator("[id=\"popover-fees\"]").click()
        self.frame_path.locator("button:has-text(\"Credit card\")").click()

    def credit_card(self):
        self.frame_path.frame_locator("iframe[title=\"Secure card number input frame\"]").locator(
            "[placeholder=\"Card number\"]").fill("4242 4242 4242 4242")
        self.frame_path.frame_locator(
            "iframe[title=\"Secure expiration date input frame\"]").locator(
            "[placeholder=\"MM \\/ YY\"]").fill("04 / 24")
        self.frame_path.frame_locator("iframe[title=\"Secure CVC input frame\"]").locator(
            "[placeholder=\"CVC\"]").fill("000")
        self.frame_path.locator("button:has-text(\"Continue\")").first.click()

    def personal_information(self):
        self.frame_path.locator("[placeholder=\"First name\"]").fill("tester")
        self.frame_path.locator("[placeholder=\"Last name\"]").fill("tester")
        self.frame_path.locator("[placeholder=\"Email address\"]").fill("tester@gmail.com")
        self.frame_path.locator("button:has-text(\"Donate $100/month\")").click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()