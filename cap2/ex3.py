'''
Exercicio 3 - Pagina 27

Em uma sala de aulas com 30 alunos do último ano de um Curso Técnico de Mecatrônica, foi pesquisado qual curso superior esses alunos gostariam de cursar. Dez disseram engenharia, 5 professor na área de exatas, 3 professor na área de humanas, 7 informática e os demais não haviam decidido. Organize os dados dessa pesquisa em uma tabela.
'''

import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
from src.ExtendedTexttable import ExtendedTexttable

def float2Porc(value):
    return "%.3f%%" % value
def floatFormat(value):
    return "%.3f" % value

total = 30
engenharia = 10
profExatas = 5
profHumanas = 3
informatica = 7
naoDecidiu = total - (engenharia + profExatas + profHumanas + informatica)

table1 = ExtendedTexttable()
table1.set_cols_align(["l", "r", "r", "r"])
# table1.set_cols_dtype(["t", "i", "f", "f"])
table1.set_deco(ExtendedTexttable.HEADER | ExtendedTexttable.FOOTER | ExtendedTexttable.BORDER)
table1.header(["Opinião", "Frequência", "Proporção", "Porcentagem"])

prop = engenharia / total
porc = prop * 100
table1.add_row( ["Engenharia", engenharia, floatFormat(prop), float2Porc(porc)] )

prop = profExatas / total
porc = prop * 100
table1.add_row( ["Prof. Exatas", profExatas, floatFormat(prop), float2Porc(porc)] )

prop = profHumanas / total
porc = prop * 100
table1.add_row( ["Prof. Humanas", profHumanas, floatFormat(prop), float2Porc(porc)] )

prop = informatica / total
porc = prop * 100
table1.add_row( ["Informática", informatica, floatFormat(prop), float2Porc(porc)] )

prop = naoDecidiu / total
porc = prop * 100
table1.add_row( ["Não decidiu", naoDecidiu, floatFormat(prop), float2Porc(porc)] )

prop = 1
porc = 100
table1.footer( ["Total", total, floatFormat(prop), float2Porc(porc)] )

print(table1.draw())
