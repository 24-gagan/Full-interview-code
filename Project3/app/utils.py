def even(n):
    return n % 2 == 0


def fact(num):
    if num < 0:
        return 1
    else:
        return num * fact(num - 1)


def login(username, password):
    if not username or not password:
        raise ValueError("Empty credentials")
    return username == "admin" and password == "secret"
