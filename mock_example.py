import requests
from dataclasses import dataclass
from prettyprinter import cpprint

response = requests.get('https://randomuser.me/api/')

print(response.status_code)
my_response = response.json()

@dataclass
class User:
    gender: str
    title: str
    firstname: str
    lastname: str
    email: str
    username: str


first_resp = my_response.get('results')[0]

gender = first_resp.get('gender')
title = first_resp.get('name').get('title')
firstname = first_resp.get('name').get('first')
lastname = first_resp.get('name').get('last')
email = first_resp.get('email')
username = first_resp.get('login').get('username')

user = User(gender, title, firstname, lastname, email, username)
cpprint(user)





