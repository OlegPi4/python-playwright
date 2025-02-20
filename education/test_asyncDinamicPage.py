import pytest
import asyncio
from playwright.async_api import Page, expect


# @pytest.mark.skip
async def test_timeout(page: Page):
    await page.goto('https://www.qa-practice.com')
    await page.screenshot(type='jpeg', path='screen.jpeg')

# @pytest.mark.skip
async def test_drag_and_drop(page: Page):
    await page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    await expect(page.locator('h1')).to_have_text('Drag-n-drop')
    await page.drag_and_drop('#rect-draggable', '#rect-droppable')
    await page.screenshot(type='jpeg', path='screen.jpeg')
    check_el = await page.locator('#rect-droppable > #rect-draggable')
    await expect(check_el).to_have_text('Drag me')
    
# @pytest.mark.skip
async def test_number_elements(page: Page):
    await page.goto('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
    checkboxes = await page.locator('input[type="checkbox"]')
    await print(checkboxes.count())
    await expect(checkboxes).to_have_count(3)
    await page.locator('input[type="checkbox"] >> nth=1').check()
    await page.screenshot(type='jpeg', path='screen.jpeg')

# asyncio.run(test_timeout())    
# asyncio.run(test_drag_and_drop())    
# asyncio.run(test_number_elements())    