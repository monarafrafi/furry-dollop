import functools
import time
import requests


def debug(active = True):
    def nested(fonction):
        @functools.wraps(fonction)
        def wrapper(*args, **kwargs):
            result = fonction(*args, **kwargs)
            if active:
                print(fonction.__name__)
                print(result)
            return result
        return wrapper
    return nested

def timerdecorator(my_function):
    def wrapper(*kargs, **kwargs):
        t1 = time.time()
        result = my_function()
        t2 = time.time()
        print("ma fonction a mis", t2-t1, "secondes a s'executer")
        return result
    return wrapper

@timerdecorator
def get_user():
    response = requests.get('https://randomuser.me/api')
    return response.json()

# Explications avec le canard
# on donne a debug le booleen active, et a nested la fonction get_user
# cette syntaxe correspond aux parametres de la sous fonction
# nested retourne wrapper
# on fait donc une egalite de reference de fonction entre get_user et wrapper
# get_user = debug(active=True)(get_user)




print(get_user())
