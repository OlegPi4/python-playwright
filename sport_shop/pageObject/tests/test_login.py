import pytest
from playwright.sync_api import Page
from pages.auth_Page import AuthPage


def test_login_correct_credent(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()    
    auth_page.login('oleg1pichkur@gmail.com', 'admfse01')
    auth_page.check_success_login()


def test_forfot_password(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()  
    auth_page.click_forgot_password()


def test_sign_in(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()  
    auth_page.click_sign_in()

def test_incorrorected_credent(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()    
    auth_page.login('olegich@kurail.com', 'dmfse011')
    auth_page.check_error_login('Неправильна адреса електронної пошти або пароль')