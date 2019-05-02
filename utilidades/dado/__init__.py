from utilidades import moeda


def resumo(p):
    print('=' * 25)
    print('     RESUMO DO VALOR')
    print('=' * 25)
    print(f' Preço analisado: {moeda.moeda(p)}')
    print(f' +10% no valor: {moeda.aumentar(p, True)} ')
    print(f' -5% no valor: {moeda.subtrair(p, True)} ')
    print(f' Dobro do valor: {moeda.dobro(p, True)}')
    print(f' Metade do valor: {moeda.metade(p, True)}')
    print('=' * 25)
