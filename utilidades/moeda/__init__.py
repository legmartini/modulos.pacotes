def aumentar(p, moeda=False):
    if moeda:
        return '{:.2f}'.format(p * 0.10 + p)


def subtrair(p, moeda=False):
    if moeda:
        return '{:.2f}'.format(p - (p * 0.05))


def dobro(p, moeda=False):
    if moeda:
        return '{:.2f}'.format(p * 2)


def metade(p, moeda=False):
    if moeda:
        return '{:.2f}'.format(p // 2)


def moeda(p):
    return '{:.2f}'.format(p)








