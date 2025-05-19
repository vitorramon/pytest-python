def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Número negativo não é permitido")
    else:
        return n * fatorial(n - 1)