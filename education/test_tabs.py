import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.mark.skip
def test_alert(page: Page, context: BrowserContext):
    page.goto('https://nomadlist.com/', timeout=60000)
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text('Get insured').click()
        new_page = new_tab_event.value

    new_page.get_by_role('link', name='Sign me up').click()

