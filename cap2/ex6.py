'''
Exercicio 6 - Pagina 27

O IBGE (2001) realizou uma pesquisa mensal a respeito da taxa de desemprego. Essa pesquisa indicou que esta taxa entre homens era, em 1998, de 7,08%; em 1999, de 7,05%; em 2000, de 6,5%, e em 2001, de 5,0%. Já para as mulheres a taxa de desemprego foi de 8,34%, em 1998; 8,27%, em 1999; 8,0%, em 2000, e 6,7%, em 2001. Construa uma tabela para apresentar esses índices e comente os resultados.
'''

import os, sys
import math
from functools import reduce

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
from src.ExtendedTexttable import ExtendedTexttable

def float2Porc(value):
    return "%.2f%%" % value
def floatFormat(value):
    return "{0:.2f}".format(value)

anoInicial = 1998
dadosHomem = [7.08, 7.05, 6.5, 5]
dadosMulher = [8.34, 8.27, 8, 6.7]

table1 = ExtendedTexttable()
table1.set_cols_align(["r", "r", "r", "r", "r"])
table1.set_cols_dtype(['t','t','t','t','t'])
table1.header(["Ano", "Homem", "Mulher", "Somatório", "Média"])
# table1.set_cols_width([5, 5, 6, 10, 10])
table1.set_deco(ExtendedTexttable.HEADER | ExtendedTexttable.FOOTER | ExtendedTexttable.BORDER)

for i, dado in enumerate(dadosHomem):
    soma = dado + dadosMulher[i]
    media = soma / 2

    table1.add_row( [
        anoInicial + i,
        floatFormat(dado),
        floatFormat(dadosMulher[i]),
        floatFormat(soma),
        floatFormat(media)
    ] )

mediaHomem = reduce(lambda x, y: x + y, dadosHomem) / len(dadosHomem)
mediaMulher = reduce(lambda x, y: x + y, dadosMulher) / len(dadosMulher)
table1.footer([ "Média", floatFormat(mediaHomem), floatFormat(mediaMulher), "-", "-"])

print(table1.draw())
