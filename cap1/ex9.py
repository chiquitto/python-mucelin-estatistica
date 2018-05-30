'''
Exercicio 9 - Pagina 19
Com a utilização de uma calculadora científica ou uma tabela de números randômicos, selecione uma amostra com 30 máquinas de soldagem, selecionadas a partir de um lote de 200 máquinas produzidas por uma indústria. Considere que as máquinas do referido lote são numeradas de 1 a 200.
'''

# from random import random, randint, choice
import random

# Gerar a populacao

maxPop = 200
maxAmostra = 30

populacao = [random.randint(0, 1000) for x in range(maxPop)]
amostrasK = sorted(random.sample(range(maxPop), maxAmostra))

# print(populacao)
print(amostrasK)

for i in amostrasK:
    print( 'Amostra %d = %d' % (i, populacao[i]) )