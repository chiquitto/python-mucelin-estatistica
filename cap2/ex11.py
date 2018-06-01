'''
Exercicio 11 - Pagina 28

Construa uma tabela com duas colunas e insira como título da primeira a palavra ORDEM e, da segunda, a palavra VALORES. Depois faça o lançamento de um dado não viciado (6 faces numerados de 1 a 6) 20 vezes. Registre os valores na tabela e faça a contagem da frequência para cada um dos valores observados nos lançamento.
'''

import os, sys
import math, random

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
from src.ExtendedTexttable import ExtendedTexttable
import tabelas.tabela5 as tabela5

def float2Porc(value):
    return "%.4f%%" % value
def floatFormat(value):
    return "%.4f" % value

total = 20
dados = [random.randint(1, 6) for i in range(total)]

# print("dados:", sorted(dados))

classes = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

for valor in dados:
    classes[valor] += 1

table1 = ExtendedTexttable()
table1.set_cols_align(["l", "r", "r"])
table1.set_cols_dtype(["t", "i", "t"])
table1.set_deco(ExtendedTexttable.HEADER | ExtendedTexttable.FOOTER | ExtendedTexttable.BORDER)
table1.header(["#", "Frequência", "Proporção"])

for key, value in classes.items():

    prop = value / total
    
    table1.add_row( [key, value, floatFormat(prop)] )

table1.footer( ["Total", total, floatFormat(1)] )

print(table1.draw())
