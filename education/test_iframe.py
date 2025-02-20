import pytest
from time import sleep
from playwright.sync_api import Page

@pytest.mark.skip
def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com')
    page.get_by_role('link', name='Text input').click()
    page.get_by_role('link', name='Iframes').click()
    # загрузка iframe
    # page.locator('.navbar-toggler-icon').click()  // так не увидит
    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()
    sleep(2)
@pytest.mark.skip
def test_select(page: Page):
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html', timeout=80000)
    page.locator('#sorter').first.select_option('Price')