import re
from playwright.sync_api import expect
from pages.base_page import BasePage

class CheckBoxes(BasePage):

    url = '/checkbox/mult_checkbox'
    locator1 = '#id_checkboxes_0'
    locator2 = '#id_checkboxes_1'
    text = 'Checkboxes'
    result_locarot = '#result-text'
    text_result = 'one, two'
    
    def is_loaded_page(self):
        title = self.page.locator('h1')
        print(title.inner_text())
        #expect(self.page).to_have_url(re.compile(self.url))         
        expect(title).to_have_text(self.text)         
    
    def click_checkBox_0(self):
        checkbox = self.page.locator(self.locator1)
        checkbox.click()
    def click_checkBox_1(self):
        checkbox = self.page.locator(self.locator2)
        checkbox.click()
         
    
    def submit_checked(self):
        submit_button = self.page.locator('input[type="submit"]')
        submit_button.click()

    def check_checkboxes_is_checked(self):
        checkbox = self.page.locator(self.result_locarot)
        print(checkbox.inner_text())
        expect(checkbox).to_have_text(self.text_result)
        
