'''
Exercicio 3 - Pagina 39

A tabela a seguir apresenta dados de habitacao no Brasil.

Com base na tabela construa:

a. Gráfico de barras dos domicilios brasileiros, segundo os anos de 1997 a 2001.
b. Gráficos de pizza para a % de domicílios rurais e urbanos, entre 1997 e 2001.
c. Gráfico de dispersão para o número de domicílios brasileiros entre os anos de 1997 e 2001.
d. Construa gráficos para representar as características dos domicílios brasileiros, segundo os anos em questão.
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

# Rede geral de abastecimento de água
abastecimentoAgua = {
	1997: 77.71,
	1998: 78.8,
	1999: 79.8,
	2001: 81.1
}

# Rede geral de esgotamento sanitário
esgotamentoSanitario = {
	1997: 40.75,
	1998: 42.4,
	1999: 64.7,
	2001: 66.7
}

# Coleta de lixo
coletaLixo = {
	1997: 68.77,
	1998: 78.3,
	1999: 80.,
	2001: 83.2
}

# Iluminação elétrica
iluminacaoEletrica = {
	1997: 93.34,
	1998: 94.2,
	1999: 94.8,
	2001: 96.
}

# Telefone
telefone = {
	1997: 27.87,
	1998: 32.,
	1999: 37.6,
	2001: 58.9
}