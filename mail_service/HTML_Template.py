"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

Reference:
    https://github.com/Knio/dominate

"""

import dominate
from dominate.tags import *
import os


def create_template_html(announcements):
    base_url = "https://mysu.sabanciuniv.edu"
    # print("HTML_TEMPLATE\n")
    doc = dominate.document(title='MySU Anouncement Notifications')

    with doc.head:
        style("""\
        h1{
            text-align:center;
        }
        
        .header1{	
            text-decoration: none !important;
            color:red	
        }
        
        .header2{
            color: DodgerBlue
        }
        
        img{
            display: block;
            margin-left: auto;
            margin-right: auto
        }
        
        #footer{
            margin-top: 0px;
            margin-bottom: 0px;
            padding-bottom: 25px;
            padding-top: 25px;
            text-align:center;
            background-color: lightblue;
        }
        
        .footer_ref{
            color: indigo;
        }
        """)
        # script(type='text/javascript', mail_service='script.js')

    with doc:
        with div(id='header'):
            img(id="icon", src="https://image.winudf.com/v2/image1/ZWR1LnNhYmFuY2l1bml2Lm15c3VfaWNvbl8xNTY3MDE5NDI1XzAwOA/icon.png?w=170&fakeurl=1")
            h1(a("mySU Notifications", href="https://mysu.sabanciuniv.edu/announcements/en", cls="header1"))
        hr(cls="rounded")

        with div(id="content"):
            for key in announcements:
                h2(a(key[0], href=base_url + key[1], cls="header2"))
                div(dominate.util.raw(str(announcements[key])))
                hr(cls="dashed")

        with div(id="footer"):
            td(a('Github: giraycoskun', href='https://github.com/giraycoskun', cls="footer_ref"))
            br()
            br()
            td(a('giraycoskun@sabanciuni.edu', href='mailto:giraycoskun@sabanciuni.edu', cls="footer_ref"))

    # print(doc)
    filename = os.path.join('mail_service','announcement.html')
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(doc.render())

    return doc.render()
