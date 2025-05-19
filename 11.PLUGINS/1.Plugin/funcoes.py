def email_valido(email):
    return "@" in email and "." in email.split("@")[-1]

def dividir(a, b):
    if b == 0:
        return None
    return a/b