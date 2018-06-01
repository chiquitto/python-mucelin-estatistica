'''
Exercicio 9 - Pagina 28

Organize os dados abaixo em uma tabela de distribuição de frequência, contendo o intervalo de classe, a frequência absoluta, a frequência acumulada, a frequência relativa, e a frequência relativa acumulada.

20.4, 22.3, 23.1, 23.5, 23.8, 24.1, 24.3, 24.3, 24.6, 24.8
24.9, 25.0, 25.1, 25.3, 25.3, 25.4, 25.6, 25.7, 25.8, 26.0
26.0, 26.1, 26.2, 26.2, 26.3, 26.5, 26.6, 26.7, 26.8, 26.9
27.1, 27.1, 27.3, 27.5, 27.7, 27.9, 28.0, 28.3, 28.7, 29.6
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

dados = [20.4, 22.3, 23.1, 23.5, 23.8, 24.1, 24.3, 24.3, 24.6, 24.8,
    24.9, 25.0, 25.1, 25.3, 25.3, 25.4, 25.6, 25.7, 25.8, 26.0,
    26.0, 26.1, 26.2, 26.2, 26.3, 26.5, 26.6, 26.7, 26.8, 26.9,
    27.1, 27.1, 27.3, 27.5, 27.7, 27.9, 28.0, 28.3, 28.7, 29.6]
total = len(dados)

valorMin = min(dados)
valorMax = max(dados)

# Determinar numero de classes (pagina 24)
numeroClasses = 1 + math.floor(3.3 * math.log(total, 10))
# numeroClasses = math.ceil(math.sqrt(total))

# Determinar intervalos entre classes (pagina 24)
amplitude = valorMax - valorMin
intervalo = round(amplitude / numeroClasses, 3)
ultimaClasse = numeroClasses - 1

print("dados:", sorted(dados))
print("numeroClasses: %f" % numeroClasses)
print("amplitude: %f (%f ~ %f)" % (amplitude, valorMin, valorMax))
print("intervalo: %f" % intervalo)

# Determinar as classes
classes = []
classeInicio = valorMin
for i in range(numeroClasses):
    classeFim = classeInicio + intervalo
    classes.append( {"inicio": classeInicio, "fim": classeFim, 'contador': 0} )
    classeInicio = classeFim

for item in dados:
    for key, classe in enumerate(classes):
        if key == ultimaClasse:
            classe['contador'] += 1
        elif classe['inicio'] <= item < classe['fim']:
            classe['contador'] += 1
            break

table1 = ExtendedTexttable()
table1.set_cols_align(["l", "r", "r", "r", "r"])
table1.set_cols_dtype(["t", "i", "i", "t", "t"])
table1.set_deco(ExtendedTexttable.HEADER | ExtendedTexttable.FOOTER | ExtendedTexttable.BORDER)
table1.header(["Opinião", "Frequência", "Frequência\nAcumulada", "Proporção", "Proporção\nAcumulada"])

freqAcumulada = 0
propAcumulada = 0
for key, classe in enumerate(classes):
    if key == ultimaClasse:
        txt = ("%.3f ou mais") % (classe['inicio'])
    else:
        txt = ("%.3f |----- %.3f") % (classe['inicio'], classe['fim'])

    freqAcumulada += classe['contador']
    prop = classe['contador'] / total
    propAcumulada += prop
    
    table1.add_row( [txt, classe['contador'], freqAcumulada, floatFormat(prop), floatFormat(propAcumulada)] )

table1.footer( ["Total", freqAcumulada, freqAcumulada, floatFormat(propAcumulada), floatFormat(propAcumulada)] )

print(table1.draw())
