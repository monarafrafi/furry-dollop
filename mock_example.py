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

    @classmethod
    def create_from_api(cls,response):
        first_resp = response.get('results')[0]
        cpprint(response)

        gender = first_resp.get('gender')
        title = first_resp.get('name').get('title')
        firstname = first_resp.get('name').get('first')
        lastname = first_resp.get('name').get('last')
        email = first_resp.get('email')
        username = first_resp.get('login').get('username')

        return User(gender, title, firstname, lastname, email, username)


class APIUnreachableException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.custom_message = "Arf, c'est pas si grave"

class HttpNotFound(Exception):
    pass


def get_user():

        try:
            response = requests.get('https://randomuser.me/api')
            print(response.status_code)

            if response.status_code == 404:
                raise HttpNotFound()

            return User.create_from_api(response.json())

        except requests.exceptions.ConnectionError as connect_error:
            print(str(connect_error))
            raise APIUnreachableException("Aie Caramba")

        finally:
            print("No matter what, I must print this! ")


def main():
    try:
        user = get_user()
        cpprint(user)

    except APIUnreachableException as e:
        print("le serveur est injoignable", str(e), e.custom_message)
    except HttpNotFound:
        print("L'information n'existe pas")


if __name__ == '__main__':
    main()



