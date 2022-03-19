import string
import random

CHARACTERS = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def random_password():
    size = random.randint(10, 20)
    password = [random.choice(CHARACTERS) for i in range(1, 20)]
    return password
