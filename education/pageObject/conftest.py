# conftest.py 
import pytest
from playwright.sync_api import Page 

@pytest.fixture
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1000, 'width': 1920})
    yield page

