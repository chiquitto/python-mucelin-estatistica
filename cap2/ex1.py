'''
Exercicio 1 - Pagina 26
Construa as tabelas de distribuição de frequência proporcional e percentual para as variáveis "sexo" e "religiao" com os dados da tabela 5.
'''

import sys
# sys.path.insert(0, '../tabelas')
sys.path.insert(0, '/home/alisson/work/python-mucelin-estatistica/tabelas')

# print(sys.path.__str__())

import tabela5

print(tabela5.createTabela())