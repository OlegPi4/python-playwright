import pytest
from playwright.sync_api import Page
from pages.auth_Page import AuthPage


data_login_correct = [('oleg1pichkur@gmail.com', 'admfse01', 'auth/profile')]
data_login_incorrect = [
    (1, 'oleg1phkur@gmail.com', 'dmfse01', 'Неправильна адреса електронної пошти або пароль'),
    (2, 'oleg1phkur@gm.ua', 'dm1,1e', 'Пароль може містити лише літери, цифри та символи'),
    (3, 'oleg1phkur@gmailfr.com', '!!', 'Пароль повинен містити не менше 6 символів'),
    (4, '', 'jjrgldf!!', "Це поле обов'язкове"),
    (5, '  ', 'jjrgldf!!', "Це поле обов'язкове"),
    (6, 'oleg1phkur@gmail.com', '', "Це поле обов'язкове"),
    (7, 'oleg1phkur@gmail.com', '  ', "Це поле обов'язкове"),
    (8, 'oleg1phkur@gmail', 'admfse01  ', "Невірний формат адреси електронної пошти"),
    (9, 'oleg1phkur@gm.ua', 'фуm11e', 'Пароль може містити лише літери, цифри та символи'),
    # (10, 'oleg1phkur@gm.ua', 'фуm11e', 'invoke error'),
    ]

# @pytest.mark.skip
@pytest.mark.parametrize("email, password, expected", data_login_correct)
def test_login_correct_credent(page: Page, email, password, expected):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()    
    auth_page.login(email, password)
    auth_page.check_success_login(expected)

# @pytest.mark.skip
def test_forfot_password(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()  
    auth_page.click_forgot_password()

# @pytest.mark.skip
def test_sign_in(page: Page):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()  
    auth_page.click_sign_in()

@pytest.mark.parametrize("id, email, password, expected", data_login_incorrect)
def test_incorrorected_credent(page: Page, id, email, password, expected):
    auth_page = AuthPage(page)
    auth_page.open_ang_check_page()    
    auth_page.login(email, password)
    auth_page.check_error_login(id, expected)