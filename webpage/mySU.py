"""
@author: Giray Coskun
@github: https://github.com/giraycoskun
"""
from webpage.WebPage import WebPage
from bs4 import BeautifulSoup


class MySU(WebPage):
    def __init__(self, url, user_agent):
        WebPage.__init__(self, url, user_agent)
        self.username = ""
        self.password = ""
        self.cas_url = "https://login.sabanciuniv.edu/cas/login"
        return

    def set_authorization(self, auth):
        self.username = auth[0]
        self.password = auth[1]

    def set_login_url(self, login_url):
        self.cas_url = login_url

    def __form_data__(self, execution):
        data = {
            'username': self.username,
            'password': self.password,
            'execution': execution,
            '_eventId': 'submit',
            'geolocation': ''
        }
        return data

    def login(self):
        response = self.session.get(self.cas_url)
        if response.status_code != 200 and response.status_code != 320:
            raise Exception("StatusCode")

        soup = BeautifulSoup(response.text, 'html.parser')
        execution = soup.find_all('input', {'name': 'execution'})[-1].attrs['value']
        data = self.__form_data__(execution)
        response = self.session.post(self.cas_url, data=data)
        #self.display(response.content)
        #self.set_page(response)
        return self.session
