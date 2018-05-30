'''
Exercicio 10 - Pagina 19
Descreva o procedimento e organize uma amostra sistemática de residências a serem pesquisadas, a partir de uma lista de casas de um bairro. Considere que as residências estão numeradas entre 300 e 500, com intervalos de 10, ou seja, {300; 310; 320; ...; 490; 500}.
'''

import numpy, random

# Definir a populacao
# residencias = numpy.arange(300, 501, 10)
residencias = list(range(300, 500, 10))

# Tamanho da populacao
totalPopulacao = len(residencias)

# Tamanho da amostra
totalAmostra = 5

step = int(totalPopulacao / totalAmostra)
first = random.randint(0, step)

print('populacao: %s' % ','.join(str(x) for x in residencias))
print('totalPopulacao: %d' % totalPopulacao)
print('totalAmostra: %d' % totalAmostra)
print('step: %d' % step)
print('first: %d' % first)

# selecionar a amostra
amostra = list(range(first, totalPopulacao, step))

print('amostra: %s' % ','.join(str(x) for x in amostra))
