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