'''
Exercicio 1 - Pagina 26
Construa as tabelas de distribuição de frequência proporcional e percentual para as variáveis "sexo" e "religiao" com os dados da tabela 5.
'''

import os, sys
# from beautifultable import BeautifulTable
# from tabulate import tabulate
from texttable import Texttable
from collections import Counter
import copy

sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))

import tabelas.tabela5 as tabela5

tabela = tabela5.createTabela()

total = len(tabela)

# Criar contadores iniciados em 0 (zero)
counterSexo = {member.value:0 for name, member in tabela5.SexoEnum.__members__.items()}
counterReligiao = {member.value:0 for name, member in tabela5.ReligiaoEnum.__members__.items()}

# Fazer as contagens em sexo e religiao
for item in tabela:
    counterSexo[item.sexo.value] += 1
    counterReligiao[item.religiao.value] += 1

# Mostrar tabela para variavel sexo

table1 = Texttable()
table1.set_cols_align(["l", "r", "r", "r"])
table1.set_cols_dtype(["t", "i", "f", "f"])
table1.set_deco(Texttable.HEADER)

table2 = copy.deepcopy(table1)

table1.header(["Sexo", "Frequência", "Proporção", "Porcentagem"])
for sexo in counterSexo:
    value = counterSexo[sexo]
    proporcao = value / total
    porc = proporcao * 100

    table1.add_row( [ tabela5.SexoEnum(sexo).name, value, proporcao, porc ] )
table1.add_row( [ "Total", total, 1, 100 ] )

table2.header(["Religião", "Frequência", "Proporção", "Porcentagem"])
for religiao in counterReligiao:
    value = counterReligiao[religiao]
    proporcao = value / total
    porc = proporcao * 100

    table2.add_row( [ tabela5.ReligiaoEnum(religiao).name, value, proporcao, porc ] )
table2.add_row( [ "Total", total, 1, 100 ] )

print ("Distribuição por sexo")
print (table1.draw())

print ("\n")

print ("Distribuição por religião")
print (table2.draw())