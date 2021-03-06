#!/usr/bin/env python
import cgitb
cgitb.enable()
import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
import cgi
form = cgi.FieldStorage()
import Cookie
import os
import json

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

my_email = cookie['email'].value
my_services = form['service'].value

data = {}

c.execute("UPDATE users SET service = ? WHERE email = ?;", (my_services, my_email))
conn.commit()

data['verify'] = "OK"

print "Content-Type: text/html"
print

print json.dumps(data)

conn.close()