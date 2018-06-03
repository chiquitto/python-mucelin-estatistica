'''
Exercicio 2 - Pagina 38

Os alunos de um determinado Instituto Federal realizaram uma prova de Física e obtiveram as seguintes notas:

5, 8, 5, 6, 7, 5, 6, 8
4, 7, 5, 5, 5, 8, 5, 6
2, 5, 6, 0, 6, 5, 6, 7
6, 6, 7, 2, 7, 6, 8, 3
4, 9, 0, 1, 7, 6, 3, 4

Construa, a partir dessas notas, os gráficos de:
a. Dispersão
b. Polígono de frequência
c. Frequência acumulada
d. Histograma
e. Pictograma
'''

import os, sys
import random
import numpy as np
from matplotlib import pyplot as plt

dados = [
	5, 8, 5, 6, 7, 5, 6, 8,
	4, 7, 5, 5, 5, 8, 5, 6,
	2, 5, 6, 0, 6, 5, 6, 7,
	6, 6, 7, 2, 7, 6, 8, 3,
	4, 9, 0, 1, 7, 6, 3, 4
]
# dados = [random.randint(0, 10) for i in range(len(dados))]
dadosMin = min(dados)
dadosMax = max(dados)

# a. Dispersao (Scatter)
x = np.arange(len(dados))
# x = list(range(len(dados)))
print(x)

path = os.path.realpath(os.path.dirname(__file__) + "/img")

# plt.scatter(x, dados, s=240, marker='+', linewidths=2)
plt.scatter(x, dados)
plt.grid(True)
plt.savefig('%s/ex2-scatter.png' % path)
# plt.show()
plt.close()

# b. Poligono de frequencia

# Encontrar as frequencias de dados
dadosFrequency = {x: dados.count(x) for x in range(0, dadosMax + 1)}
# dadosFrequency = collections.Counter(dados)

x, y = ([], [])
for key, value in dadosFrequency.items():
	x.append(key)
	y.append(value)

plt.plot(y)
plt.grid(True)
# plt.axis([0, 10, 0, max(y)])
plt.ylabel('frequência')
plt.savefig('%s/ex2-poligono-frequencia.png' % path)
# plt.show()
plt.close()

# c. Frequência acumulada

# Acumular as frequencias
dadosFrequency = []
for x in range(0, dadosMax + 1):
	if x == 0:
		dadosFrequency.append(dados.count(x))
	else:
		dadosFrequency.append(dados.count(x) + dadosFrequency[x - 1])

plt.plot(dadosFrequency)
plt.grid(True)
# plt.axis([0, 10, 0, max(y)])
plt.ylabel('frequência')
plt.savefig('%s/ex2-poligono-frequencia-acumulada.png' % path)
# plt.show()
plt.close()

# d. Histograma
plt.grid(True)
plt.hist(dados, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.savefig('%s/ex2-histograma.png' % (path))
plt.close()

# e. Pictograma
plt.bar(list(range(0, dadosMax + 1)), y)
plt.grid(True)
plt.ylabel('frequência')
plt.savefig('%s/ex2-bar.png' % path)
# plt.show()
plt.close()