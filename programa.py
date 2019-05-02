from utilidades import dado
from utilidades import moeda

while True:
    p = input('Preço R$ ')
    if p == '' or not p.isnumeric():
        print('Valor não inserido ou inválido.')
    else:
        dado.resumo(float(p))




