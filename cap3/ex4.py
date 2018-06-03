'''
Exercicio 4 - Pagina 40

Em um mercado de telefones celulares de uma região do Brasil, considerando-se uma fatia de mercado meramente ilustrativa, obtiveram-se os resultados conforme descritos na tabela:

Marcas		Participação no mercado
Nokia			 60%
Ericson			 20%
Gradiente		 15%
Philips			  5%
Total			100%
'''

import os, sys, locale
import numpy as np

from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt

path = os.path.realpath(os.path.dirname(__file__) + "/img")
locale.setlocale(locale.LC_ALL, 'pt_BR')

def pizza():
	explode = (0.1, 0, 0, 0)

	fig1, ax1 = plt.subplots()
	ax1.pie(participacao, explode=explode, labels=marcas, autopct='%1.1f%%',
			shadow=True, startangle=90)

	plt.title('Participação no mercado/marca')

	plt.savefig('%s/ex4-pizza.png' % path)
	# plt.show()
	plt.close()

def colunas():
	formatter = FuncFormatter(colunasTicker)

	fig1, ax1 = plt.subplots()

	ax1.yaxis.set_major_formatter(formatter)

	pos_x = np.arange(len(tabela))
	ax1.bar(pos_x, participacao)

	ax1.set_xlabel('marca')
	ax1.set_ylabel('participação (%)')

	plt.title('Participação no mercado/marca')
	plt.xticks(pos_x, marcas)

	plt.savefig('%s/ex4-coluna.png' % path)
	# plt.show()
	plt.close()

def colunasTicker(x, pos):
    return '{0:n}%'.format(x * 100)

tabela = (
	{'marca': "Nokia", 'participacao': .6},
	{'marca': "Ericson", 'participacao': .2},
	{'marca': "Gradiente", 'participacao': .15},
	{'marca': "Philips", 'participacao': .05}
)
marcas = [value['marca'] for value in tabela]
participacao = [value['participacao'] for value in tabela]

pizza()
colunas()
