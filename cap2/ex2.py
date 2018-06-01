'''
Exercicio 2 - Pagina 27

Considere que em uma pesquisa de opinião realizada com 2000 pessoas a respeito da privatização de uma das maiores empresas brasileiras de extração de minérios, as opiniões foram: 630 favoráveis à privatização, 1053 contrárias, 117 não quiseram se manifestar e os demais disseram não saber opinar. Organize o resultado dessa pesquisa em uma tabela.
'''

import os, sys
from texttable import Texttable

def float2Porc(value):
    return "%.3f%%" % value
def floatFormat(value):
    return "%.3f" % value

total = 2000
favoraveis = 630
desfavoraveis = 1053
naoQuiseramOpinar = 117
naoSabeOpinar = total - (favoraveis + desfavoraveis + naoQuiseramOpinar)

table1 = Texttable()
table1.set_cols_align(["l", "r", "r", "r"])
# table1.set_cols_dtype(["t", "i", "f", "f"])
table1.set_deco(Texttable.HEADER)
table1.header(["Opinião", "Frequência", "Proporção", "Porcentagem"])

prop = favoraveis / total
porc = prop * 100
table1.add_row( ["Favoráveis", favoraveis, floatFormat(prop), float2Porc(porc)] )

prop = desfavoraveis / total
porc = prop * 100
table1.add_row( ["Contrários", desfavoraveis, floatFormat(prop), float2Porc(porc)] )

prop = naoQuiseramOpinar / total
porc = prop * 100
table1.add_row( ["Não quiseram se manifestar", naoQuiseramOpinar, floatFormat(prop), float2Porc(porc)] )

prop = naoSabeOpinar / total
porc = prop * 100
table1.add_row( ["Não souberam opinar", naoSabeOpinar, floatFormat(prop), float2Porc(porc)] )

prop = 1
porc = 100
table1.add_row( ["Total", total, floatFormat(prop), float2Porc(porc)] )

print(table1.draw())
