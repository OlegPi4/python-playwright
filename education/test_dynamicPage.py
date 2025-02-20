import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_timeout(page):
    page.goto('https://www.qa-practice.com')
    page.screenshot(type='jpeg', path='screen.jpeg')

@pytest.mark.skip
def test_drag_and_drop(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    expect(page.locator('h1')).to_have_text('Drag-n-drop')
    page.drag_and_drop('#rect-draggable', '#rect-droppable')
    page.screenshot(type='jpeg', path='screen.jpeg')
    check_el = page.locator('#rect-droppable > #rect-draggable')
    expect(check_el).to_have_text('Drag me')
    
def test_number_elements(page: Page):
    page.goto('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
    checkboxes = page.locator('input[type="checkbox"]')
    print(checkboxes.count())
    expect(checkboxes).to_have_count(3)
    page.locator('input[type="checkbox"] >> nth=1').check()
    page.screenshot(type='jpeg', path='screen.jpeg')