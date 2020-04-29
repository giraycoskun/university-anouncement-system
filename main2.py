"""
@author: Giray Coskun
@github: https://github.com/giraycoskun
"""
import requests
import bs4
import webbrowser


def display(content):
    # to see this HTML in web browser
    with open('temp.html', 'wb') as f:
        f.write(content)
        webbrowser.open('temp.html')


with requests.session() as r:
    LOGIN = "giraycoskun"
    PASSWORD = "18GCsabanci"

    login_url = "https://login.sabanciuniv.edu/cas/login"
    profile_url = "https://mysu.sabanciuniv.edu/announcements/en/all"

    # session need it only once and it will remember it
    r.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    })

    # load page with form - to get cookies and `csrf` from HTML
    response = r.get(login_url)

    # display(response.content)

    # get `csrf` from HTML
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    csrf = soup.find_all('input', {'name': 'execution'})[-1].attrs['value']

    print('csrf:', csrf)

    # cookies are not part of form so you don't use in form_data,
    # session will use cookies from previous request so you don't have to copy them
    form_data = {
        'username': LOGIN,
        'password': PASSWORD,
        'execution': csrf,
        '_eventId': 'submit',
        'geolocation': '',
    }

    # send form data to server
    response = r.post(login_url, data=form_data)

    print('status_code:', response.status_code)
    print('history:', response.history)
    print('url:', response.url)

    display(response.content)

    response = r.get(profile_url)

    display(response.content)
