'''
Exercicio 8 - Pagina 19
Em um IF do Brasil estão matriculados 1200 alunos.
Sabendo-se que 800 são moças e 400 rapazes, descreva o procedimento para selecionar uma amostra estratificada proporcional a 10% desses alunos, segundo o gênero.
'''

mocas = 800
rapazes = 400
total = mocas + rapazes
porc = 10 # encontrar 10%

porcMocas = porc * mocas / 100
porcRapazes = porc * rapazes / 100

print(porcMocas)
print(porcRapazes)