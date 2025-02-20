import pytest
from playwright.async_api import async_playwright, expect


# @pytest.mark.skip

@pytest.mark.asyncio
async def test_timeout():
    async with async_playwright() as p:
        chromium = p.chromium # or "firefox" or "webkit".
        browser = await chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com')
        await page.screenshot(type='jpeg', path='screen.jpeg')
        


@pytest.mark.asyncio
async def test_drag_and_drop():
    async with async_playwright() as p:
        chromium = p.chromium # or "firefox" or "webkit".
        browser = await chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
        await expect(page.locator('h1')).to_have_text('Drag-n-drop')
        await page.drag_and_drop('#rect-draggable', '#rect-droppable')
        await page.screenshot(type='jpeg', path='screen.jpeg')
        check_el =  page.locator('#rect-droppable > #rect-draggable')
        await expect(check_el).to_have_text('Drag me')
        


@pytest.mark.asyncio
async def test_number_elements():
    async with async_playwright() as p:
        chromium = p.chromium # or "firefox" or "webkit".
        browser = await chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
        checkboxes = page.locator('input[type="checkbox"]')
        print(checkboxes.count())
        await expect(checkboxes).to_have_count(3)
        await page.locator('input[type="checkbox"] >> nth=1').check()
        await page.screenshot(type='jpeg', path='screen.jpeg')
        await browser.close()

