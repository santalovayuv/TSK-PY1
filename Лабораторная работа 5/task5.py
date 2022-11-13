import random
import string


def random_password(n=8) -> str:
#TODO написать функцию генерациислучайных паролей
    if not isinstance(n, int):
        raise TypeError("y переменной n должен быть тип int")
    if not n > 0:
        raise ValueError("Количество символов должно быть больше нуля")
    list_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    list_password = random.sample(list_, n)
    password = "". join(list_password)
    return password


print(random_password())
