'''
Exercicio 3 - Pagina 39

A tabela a seguir apresenta dados de habitacao no Brasil.

Com base na tabela construa:

a. Gráfico de barras dos domicilios brasileiros, segundo os anos de 1997 a 2001
b. Gráficos de pizza para a % de domicílios rurais e urbanos, entre 1997 e 2001
c. Gráfico de dispersão para o número de domicílios brasileiros entre os anos de 1997 e 2001
'''

import os, sys, locale

path = os.path.realpath(os.path.dirname(__file__) + "/img")
locale.setlocale(locale.LC_ALL, 'pt_BR')

numeroDomicilios = {
	1997: 40644623,
	1998: 41839703,
	1999: 43859738,
	2001: 46579967
}

porcDomiciliosUrbano = {
	1997: 81.14,
	1998: 81.2,
	1999: 81.4,
	2001: 85.2
}

porcDomiciliosRural = {
	1997: 18.86,
	1998: 18.8,
	1999: 18.6,
	2001: 14.8
}