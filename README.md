# Announcement Notification System for University Announcements

A System to track announcements from a website with Central Authentication System(CAS) such as university acounts

Developed for Sabancı University(mySU)
[https://mysu.sabanciuniv.edu/](https://mysu.sabanciuniv.edu/)


#### Notes:

- Required to install [https://github.com/Knio/dominate](https://github.com/Knio/dominate)
- Change passwords.template to passwords.txt with valid passwords
- Change mail_service/last_announcements.template to mail_service/last_announcements.json
- Change mail_service/mail_list.template to mail_service/mail_list.txt with valid mail adresses
- For sender Gmail server enable [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps)
- Works with [Task Scheduler](https://martechwithme.com/schedule-python-scripts-windows-mac/)
- localhost server command: python -m smtpd -c DebuggingServer -n localhost:1025 (windows: cmd)

---

### Directory Structure:

- [main.py](https://github.com/giraycoskun/University-Anouncement-System/blob/master/main.py)

- [mail_service](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service)
    - creates template html [HTML_Template.py](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/HTML_Template.py)
    - sends email to receiver emails [Announcement_Mail_Server.py](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/Announcement_Mail_Server.py)
    - keeps data to already sent announcements [last_announcements.json](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/last_announcements.template)
    - keeps mail list both sender and receivers [mail_list.txt](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/mail_list.templated)

- [webpage](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage)
    - [WebPage Class](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage/WebPage.py)
    - [MySU SubClass](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage/mySU.py)
    
- [main2.py](https://github.com/giraycoskun/University-Anouncement-System/blob/master/main2.py) Keeps a simpler version

- [passwords.txt](https://github.com/giraycoskun/University-Anouncement-System/blob/master/passwords.template) Keeps passwords

- [log.json](https://github.com/giraycoskun/University-Anouncement-System/blob/master/log.json) Keeps Logs

---
### Class: Website
#### Properties:
* user_agent
* session
* URL
* COUNT
* current_page
* soup
#### Methods:
* \_\_init__(url, user_agent)
* \_\_create_Session__()
* display(content)
* get_page(url)
* set_page(response)
* print_content()
* get_content()
* write_content(filename)
---

### SubClass: Mysu
#### Properties:
* user_name
* password
* cas_url
#### Methods:
* set_authorization(auth)
* set_login_url(login_url)
* \_\_form_data__(execution)
* login()

---

### Docs:
- https://docs.python.org/3/library/smtplib.html
- https://docs.python.org/3/library/email.mime.html
- https://github.com/Knio/dominate

### REFERENCE:
- https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
- https://developers.google.com/gmail/api/quickstart/python
- https://stackoverflow.com/questions/47869039/python-requests-login-with-website

---
Giray Coskun

[giraycoskun@sabanciuniv.edu](mailto:giraycoskun@sabanciuniv.edu)
