import pytest
from playwright.sync_api import Page
from pages.checkBoxe_page import CheckBoxes

@pytest.mark.skip
def test_checkboxes_exists(page: Page):
    checkboxes_page = CheckBoxes(page)
    checkboxes_page.open()
    checkboxes_page.is_loaded_page()

@pytest.mark.skip
def test_checkboxes_checked(page: Page):
    checkboxes_page = CheckBoxes(page)
    checkboxes_page.open()
    checkboxes_page.click_checkBox_0()
    checkboxes_page.click_checkBox_1()
    checkboxes_page.submit_checked()
    checkboxes_page.check_checkboxes_is_checked()