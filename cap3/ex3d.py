import ex3
from matplotlib import pyplot as plt
import numpy as np
import locale
import sys

locale.setlocale(locale.LC_ALL, 'pt_BR')

labels = (
	"Abastecimento de água",
	"Esgotamento sanitário",
	"Coleta de lixo",
	"Iluminação elétrica",
	"Telefone"
)
dados = (
	[value for key, value in ex3.abastecimentoAgua.items()],
	[value for key, value in ex3.esgotamentoSanitario.items()],
	[value for key, value in ex3.coletaLixo.items()],
	[value for key, value in ex3.iluminacaoEletrica.items()],
	[value for key, value in ex3.telefone.items()]
)

anos = [str(key) for key, value in ex3.abastecimentoAgua.items()]

colunas = len(dados)
w = .75
colunaW = w / colunas
pos_ajust = [-colunaW * 2, -colunaW, 0, colunaW, colunaW * 2]

fig, ax = plt.subplots()
pos_x0 = np.arange(len(dados[0]))

for i, (label, values) in enumerate(zip(labels, dados)):
	pos_x = pos_x0 + pos_ajust[i]

	b = ax.bar(pos_x, values, colunaW, label=label, bottom=0)

ax.set_xlabel('ano')
ax.set_ylabel('% (domicílios)')

plt.xticks(pos_x0, anos)

plt.legend(loc='lower right', ncol=2, fontsize='small')
plt.title('Características dos domicílios brasileiros/ano')

plt.savefig('%s/ex3d.png' % ex3.path)
# plt.show()
plt.close()
