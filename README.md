# Anouncement Notification System for University Anouncements developped for Sabanci University(mySU)

A System to track anouncements from a website with Central Authentication System(CAS) such as university acounts
[https://mysu.sabanciuniv.edu/](https://mysu.sabanciuniv.edu/)

---


## Classes

### Class: Website

* user_agent
* session
* URL
* COUNT
* current_page
* soup
---
* \__init__(url, user_agent)
* \__create_Session__()
* display(content)
* get_page(url)
* set_page(response)
* print_content()
* get_content()
* write_content(filename)

### SubClass: Mysu

* user_name
* password
* cas_url
---
* set_authorization(auth)
* set_login_url(login_url)
* \__form_data|||(execution)
* login()

---

Giray Coskun

<giraycoskun@sabanciuniv>
