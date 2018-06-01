'''
Exercicio 4 - Pagina 27

Elabore uma tabela de frequência proporcional e percentual para a variável "estatura" com os dados da tabela 5.
'''

import os, sys
import math

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
from src.ExtendedTexttable import ExtendedTexttable
import tabelas.tabela5 as tabela5

def float2Porc(value):
    return "%.3f%%" % value
def floatFormat(value):
    return "%.3f" % value

tabela = tabela5.createTabela()
total = len(tabela)

estaturaMin = estaturaMax = tabela[0].estatura
for item in tabela[1:]:
    estaturaMin = min(estaturaMin, item.estatura)
    estaturaMax = max(estaturaMax, item.estatura)

# Determinar numero de classes (pagina 24)
# numeroClasses = 1 + math.ceil(3.3 * math.log(total, 10))
numeroClasses = math.ceil(math.sqrt(total))

# Determinar intervalos entre classes (pagina 24)
amplitude = estaturaMax - estaturaMin
intervalo = math.ceil(amplitude / numeroClasses)

print("numeroClasses: %d" % numeroClasses)
print("amplitude: %d (%d ~ %d)" % (amplitude, estaturaMin, estaturaMax))
print("intervalo: %f" % intervalo)

# Determinar as classes
classes = []
classeInicio = estaturaMin
for i in range(numeroClasses):
    classeFim = classeInicio + intervalo
    classes.append( {"inicio": classeInicio, "fim": classeFim, 'contador': 0} )
    classeInicio = classeFim

for item in tabela:
    for classe in classes:
        if classe['inicio'] <= item.estatura < classe['fim']:
            classe['contador'] += 1

table1 = ExtendedTexttable()
table1.set_cols_align(["l", "r", "r", "r"])
# table1.set_cols_dtype(["t", "i", "f", "f"])
table1.set_deco(ExtendedTexttable.HEADER | ExtendedTexttable.FOOTER | ExtendedTexttable.BORDER)
table1.header(["Opinião", "Frequência", "Proporção", "Porcentagem"])

a = chr(195)
b = chr(196)

for classe in classes:
    txt = ("%d |----- %d") % (classe['inicio'], classe['fim'])
    prop = classe['contador'] / total
    porc = prop * 100
    table1.add_row( [txt, classe['contador'], floatFormat(prop), float2Porc(porc)] )

table1.footer( ["Total", total, floatFormat(1), float2Porc(100)] )

print(table1.draw())