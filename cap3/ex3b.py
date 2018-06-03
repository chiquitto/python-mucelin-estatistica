import ex3
from matplotlib import pyplot as plt
# import sys

print("dados:", ex3.porcDomiciliosUrbano)
print("dados:", ex3.porcDomiciliosRural)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
fig.suptitle('Situação do domicílio')

anos_pos = [[1997, 1998], [1999, 2001]]

# Cria o gráfico de pizza na primeira posição com as configurações definidas
for y_pos, y_anos_pos in enumerate(anos_pos):

	for x_pos, ano in enumerate(y_anos_pos):
		pie = ax[y_pos][x_pos].pie(
			[ex3.porcDomiciliosUrbano[ano], ex3.porcDomiciliosRural[ano]],
			# labels=['Urbano', 'Rural'],
			autopct='%1.1f%%')
		ax[y_pos][x_pos].set_title(ano)
		ax[y_pos][x_pos].axis('equal')

print(pie)
plt.figlegend(pie[0], ['Urbano', 'Rural'], loc='upper right')

plt.savefig('%s/ex3b.png' % ex3.path)
# plt.show()
