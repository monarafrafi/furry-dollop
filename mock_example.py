import requests
from dataclasses import dataclass
from prettyprinter import cpprint

@dataclass
class User:
    gender: str
    title: str
    firstname: str
    lastname: str
    email: str
    username: str


class APIUnreachableException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.custom_message = "Arf, c'est pas si grave"


def get_user_description():

        try:
            response = requests.get('https://randomuser.me/api/')

            my_response = response.json()

            first_resp = my_response.get('results')[0]

            gender = first_resp.get('gender')
            title = first_resp.get('name').get('title')
            firstname = first_resp.get('name').get('first')
            lastname = first_resp.get('name').get('last')
            email = first_resp.get('email')
            username = first_resp.get('login').get('username')

            return User(gender, title, firstname, lastname, email, username)

        except requests.exceptions.ConnectionError as connect_error:
            print(str(connect_error))
            raise APIUnreachableException("Aie Caramba")

        finally:
            print("No matter what, I must print this! ")

def main():
    try:
        user = get_user_description()
        cpprint(user)

    except APIUnreachableException as e:
        print("le serveur est injoignable", str(e), e.custom_message)


if __name__ == '__main__':
    main()



