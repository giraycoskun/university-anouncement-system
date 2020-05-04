"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

References:
    https://stackoverflow.com/questions/47869039/python-requests-login-with-website
"""

from webpage.mySU import MySU
from mail_service.HTML_Template import create_template_html
from mail_service.Announcement_Mail_Server import mail_server

url = "https://mysu.sabanciuniv.edu/announcements/en/all"
base_url = "https://mysu.sabanciuniv.edu"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 " \
             "Safari/537.36 "

user_name = ""
password = ""
with open('passwords.txt', 'r') as file:
    for line in file:
        if 'mysu_username' in line:
            user_name = line.split()[1]
        if 'mysu_password' in line:
            password = line.split()[1]

auth = (user_name, password)

page = MySU(url, user_agent)
page.set_authorization(auth)
page.login()
page.get_page()
# page.display()

announcements = page.get_announcement_list()
announcements = page.get_announcements(announcements)

# CHECK LAST ANNOUNCEMENTS
check = True
################

if check:
    # CREATE HTML TEMPLATE
    html = create_template_html(announcements)
    ################

    mail_server(html)