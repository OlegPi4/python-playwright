import pytest

class BasePage:

    base_url = 'https://teamchallenge-sport-store-frontend.vercel.app/'
    url = None   
    def __init__(self, page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(f'{self.base_url}{self.url}')
        else:
            print('The URL isn"t pointed')

    def fail_report(self, tmp_path, email, password, expected, test):
        d = tmp_path/"FailReport"
        d.mkdir()
        p = d / "report.txt"
        CONTENT = f"Test: {test}\nExpected: {expected}\nActual: {self.page.url}\nEmail: {email}\nPassword: {password}\n\n"
        p.write_text(CONTENT, encoding="utf-8")