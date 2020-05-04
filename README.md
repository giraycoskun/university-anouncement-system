# Anouncement Notification System for University Anouncements

A System to track announcements from a website with Central Authentication System(CAS) such as university acounts

Developed for Sabancı University(mySU)
[https://mysu.sabanciuniv.edu/](https://mysu.sabanciuniv.edu/)


#### Notes:

- Change passwords.template to passwords.txt with valid passwords 

- Works with [Task Scheduler](https://martechwithme.com/schedule-python-scripts-windows-mac/)

---

### Directory Structure:

- [main.py](https://github.com/giraycoskun/University-Anouncement-System/blob/master/main.py)

- [mail_service](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service)
    - creates template html [HTML_Template.py](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/HTML_Template.py)
    - sends email to receiver emails [Announcement_Mail_Server.py](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/Announcement_Mail_Server.py)
    - keeps data to already sent announcements [last_announcements.json](https://github.com/giraycoskun/University-Anouncement-System/tree/master/mail_service/last_announcements.template)

- [webpage](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage)
    - [WebPage Class](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage/WebPage.py)
    - [MySU SubClass](https://github.com/giraycoskun/University-Anouncement-System/tree/master/webpage/mySU.py)
    
- [main2.py](https://github.com/giraycoskun/University-Anouncement-System/blob/master/main2.py) Keeps a simpler version

- [passwords.txt](https://github.com/giraycoskun/University-Anouncement-System/blob/master/passwords.template) Keeps passwords

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

Giray Coskun

[giraycoskun@sabanciuniv.edu](mailto:giraycoskun@sabanciuniv.edu)
