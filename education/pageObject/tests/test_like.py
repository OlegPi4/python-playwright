import pytest
from playwright.sync_api import Page
from pages.like_page import LikeAButton

@pytest.mark.skip
def test_like_a_button_exists(page:Page):
    like_page = LikeAButton(page)
    like_page.open()
    like_page.check_button_visible()

@pytest.mark.skip
def test_like_a_button_click(page:Page):
    like_page = LikeAButton(page)
    like_page.open()
    like_page.click_button()
    like_page.check_result_text_is_('Submitted')
    
