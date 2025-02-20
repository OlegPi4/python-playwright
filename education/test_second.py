import pytest
from time import sleep
from playwright.sync_api import Page, expect, Route
import re

@pytest.mark.skip
def test_request(page: Page):

    def change_request(route: Route):
        data = route.request.post_data
        if data:
            data = data.replace('admfse01', 'dhhue12!')
        print(data)
        route.continue_(post_data=data)
    page.route(re.compile('user/login'), change_request)
    page.goto("http://localhost:3000/auth/login")
    page.get_by_label("Електронна пошта").fill('oleg1pichkur@gmail.com')
    page.get_by_label("Пароль").fill('admfse01')
    page.get_by_role('button', name="Увійти").click()
    # false
    expect(page.get_by_text('Неправильна адреса електронної пошти або пароль')).to_be_visible()                        
    # true
    # expect(page).to_have_url('http://localhost:3000/auth/profile')    
    sleep(3)

@pytest.mark.skip
def test_responce(page: Page):

    def change_response(route: Route):
        response = route.fetch()
        data = response.text()
        data = data.replace('Пічкур', 'Про100')
        print(data)
        route.fulfill(response=response, body=data)

    page.route(re.compile('user/view'), change_response)
    page.goto("http://localhost:3000/auth/login")
    page.get_by_label("Електронна пошта").fill('oleg1pichkur@gmail.com')
    page.get_by_label("Пароль").fill('admfse01')
    page.get_by_role('button', name="Увійти").click()
    expect(page).to_have_url('http://localhost:3000/auth/profile')    
    page.get_by_role('link', name="Мої данні").click()
    sleep(3)
