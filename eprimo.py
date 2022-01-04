def éPrimo(x):
    i = 2
    while x % i != 0 and i < x:
        i = i + 1
    if x % i == 0 and i < x:
        return False
    else:
        return True


def maior_primo(x):

    while éPrimo(x) == False:
        x = x - 1
    else:
        return x
