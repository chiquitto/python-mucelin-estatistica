# Exercicio 7 - Pagina 19
# Organize uma tabela de números randômicos com 10 linhas e 10 colunas, utilizando o Software Excel

from random import randint

w, h = 8, 5
Matrix = [[randint(0, 9) for x in range(w)] for y in range(h)]

# print(Matrix)

for linha in Matrix:
    for coluna in linha:
        print(coluna)
