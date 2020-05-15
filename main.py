"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

References:
    https://stackoverflow.com/questions/47869039/python-requests-login-with-website
"""

import os.path as path
import json
from datetime import date
from webpage.mySU import MySU
from mail_service.HTML_Template import create_template_html
from mail_service.Announcement_Mail_Server import mail_server

print("mySU Notification System has started")
try:
    url = "https://mysu.sabanciuniv.edu/announcements/en/all"
    base_url = "https://mysu.sabanciuniv.edu"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 " \
                 "Safari/537.36 "

    user_name = ""
    password = ""
    filename = path.join('mail_service', 'mail_list.txt')
    with open(filename, 'r') as file:
        sender_email = file.readline().rstrip()
        receiver_emails = [line.rstrip() for line in file]

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
    filename = path.join('mail_service', 'last_announcements.json')

    new_data = list()
    for key in announcements:
        temp = dict()
        temp[key[0]] = key[1]
        new_data.append(temp)

    with open(filename) as json_file:
        data = json.load(json_file)
        data = data['announcements']
        for element in new_data:
            if element in data:
                items = list(element.items())
                del announcements[items[0]]

        if len(announcements) == 0:
            check = False

    if check:
        with open(filename) as json_file:
            data = json.load(json_file)

            temp = data['announcements']

            for element in new_data:
                temp.append(element)

            if len(temp) > 30:
            	count = len(temp) - 30
            	for i in range(count):
            		temp.pop(i)

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        ################

    if check:
        # CREATE HTML TEMPLATE
        html = create_template_html(announcements)
        ################

        with open('passwords.txt', 'r') as file:
            for line in file:
                if 'mail_address' in line:
                    address = line.split()[1]
                if 'mail_password' in line:
                    password = line.split()[1]

        mail_server(html, address, password, sender_email, receiver_emails)

    # LOG
    with open('log.json') as json_file:
        data = json.load(json_file)
        temp = data['logs']
        if len(temp) == 0:
            count = 0
        else:
            count = int(temp[-1]['count'])
        if len(temp) > 30:
            temp.pop(0)

        today = date.today()
        today_str = today.strftime('%d/%m/%Y')
        count += 1
        new_log = {
            "date": today_str,
            "check": str(check),
            "count": count
        }

        if check:
            new_log['html'] = html

        temp.append(new_log)

    with open('log.json', 'w') as f:
        json.dump(data, f, indent=4)

except BaseException as e:
    print("System FAILED")
    error_message = type(e).__name__
    print(error_message)
    with open('log.json') as json_file:
        today = date.today()
        today_str = today.strftime('%d/%m/%Y')
        data = json.load(json_file)
        data['notes'].append("LAST FAILURE: " + error_message + " " + today_str)

    with open('log.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print("SYSTEM TERMINATED WITH SUCCESS")
