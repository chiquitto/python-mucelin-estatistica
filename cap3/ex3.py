'''
Exercicio 3 - Pagina 39

A tabela a seguir apresenta dados de habitacao no Brasil.

Com base na tabela construa:

a. Grafico de barras dos domicilios brasileiros, segundo os anos de 1997 a 2001
'''

import os, sys

path = os.path.realpath(os.path.dirname(__file__) + "/img")

numeroDomicilios = {
	1997: 40644623,
	1998: 41839703,
	1999: 43859738,
	2001: 46579967
}
