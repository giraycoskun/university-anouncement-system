# Anouncement Notification System for University Anouncements

A System to track anouncements from a website with Central Authentication System(CAS) such as university acounts

Developed for Sabancı University(mySU)
[https://mysu.sabanciuniv.edu/](https://mysu.sabanciuniv.edu/)


#### Notes:

- Change passwords.template to passwords.txt with valid passwords 

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
