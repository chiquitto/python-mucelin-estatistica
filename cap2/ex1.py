'''
Exercicio 1 - Pagina 26
Construa as tabelas de distribuição de frequência proporcional e percentual para as variáveis "sexo" e "religiao" com os dados da tabela 5.
'''

import os, sys

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))

import tabelas.tabela5 as tabela5

print(tabela5.createTabela())
