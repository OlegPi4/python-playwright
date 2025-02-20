import pytest
from playwright.sync_api import Page 
from pages.simple_page import SimplePage

@pytest.mark.skip
def test_simple_exists(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_exists()

@pytest.mark.skip
def test_simple_click(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.click_button()
    simple_page.check_result_text_is_('Submitted')
   