"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

Reference:
    https://requests.readthedocs.io/en/master/
"""
import webbrowser
import requests
from bs4 import BeautifulSoup


class WebPage:

    def __init__(self, url, user_agent):
        self.user_agent = user_agent
        self.session = self.__create_session__()
        self.URL = url
        self.COUNT = 0
        self.current_page = ""
        self.soup = ""
        return

    def __create_session__(self):
        session = requests.session()
        session.headers.update({
            "User-Agent": self.user_agent
        })
        return session

    def display(self, content=""):
        # to see this HTML in web browser
        if content == "":
            content = self.current_page.content
        filename = "content" + str(self.COUNT) + ".html"
        self.COUNT += 1
        with open(filename, 'wb') as f:
            f.write(content)
            webbrowser.open(filename)

    def get_page(self, url=""):
        """

        :rtype: HTML page from requests library
        """
        if url == "":
            url = self.URL
        page = self.session.get(url)
        if page.status_code == 200:
            self.current_page = page
            self.soup = BeautifulSoup(page.content, 'html.parser')
            return True
        else:
            return False

    def set_page(self, response):
        self.current_page = response
        self.soup = BeautifulSoup(self.current_page.content, 'html.parser')
        return True

    def print_content(self):
        if self.soup != "":
            print(self.soup.prettify())

    def get_content(self):
        return self.current_page.content

    def write_content(self, filename="page_output.html"):
        with open(filename, 'w') as file:
            file.write(self.current_page.text)
        return
