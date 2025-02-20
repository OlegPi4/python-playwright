import re
from playwright.sync_api import expect
from pages.base_page import BasePage

# Locators
input_email = 'css=[name="email"]'
input_password = 'css=[name="password"]'

class AuthPage(BasePage):
    url = 'auth/login'

    def open_ang_check_page(self):
        self.open()
        expect(self.page).to_have_url(re.compile(self.url))

    def enter_email(self, email): 
        username_input = self.page.locator(input_email)
        username_input.fill(email)

    def enter_password(self, password): 
        username_input = self.page.locator(input_password)
        username_input.fill(password)

    
    def click_login_button(self):
        login_button = self.page.get_by_role('button', name='Увійти' )
        login_button.click()
    
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def check_success_login(self):
        expect(self.page).to_have_url(re.compile('auth/profile'))
        
    def click_forgot_password(self):
        login_button = self.page.get_by_role('button', name='Забули пароль?' )
        login_button.click()
        el = self.page.get_by_role('button', name='Надіслати інструкцію' )
        expect(el).to_be_visible()
      
    def click_sign_in(self):
        login_button = self.page.get_by_role('button', name='Зареєструватись' )
        login_button.click()
        expect(self.page).to_have_url(re.compile('/auth/signup'))
    
    def check_error_login(self, error_mes):
        message_error = self.page.locator('.text-red')
        
        if message_error.inner_text() == error_mes:
            print(message_error.inner_text())
            expect(self.page)   
        else:
            print(message_error.inner_text())
            expect(self.page).to_have_title('!!!')
       