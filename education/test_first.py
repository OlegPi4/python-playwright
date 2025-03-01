import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_wiki1(page: Page):
    page.goto("https://wikipedia.org")
    page.get_by_role('link', name="Русский").click()
    expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()

@pytest.mark.skip
def test_wiki2(page: Page):
    page.goto("https://wikipedia.org")
    page.get_by_role('link', name="Русский").click()    
    page.get_by_role('link', name="Содержание").click()    
    page.locator('#ca-talk').click()
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')
