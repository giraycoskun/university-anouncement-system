"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

References:
    https://stackoverflow.com/questions/47869039/python-requests-login-with-website
"""

from webpage import mySU
import pprint

url = "https://mysu.sabanciuniv.edu/announcements/en/all"
base_url = "https://mysu.sabanciuniv.edu"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 " \
             "Safari/537.36 "

user_name = ""
password = ""
with open('passwords.txt', 'r') as file:
    user_name = file.readline().strip()
    password = file.readline().strip()

auth = (user_name, password)

page = mySU.MySU(url, user_agent)
page.set_authorization(auth)
page.login()
page.get_page()
#page.display()

announcements = page.get_announcement_list()
announcements = page.get_announcements(announcements)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(announcements)