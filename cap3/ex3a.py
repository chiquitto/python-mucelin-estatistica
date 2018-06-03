import ex3
from matplotlib import pyplot as plt
import locale
import sys

print("dados:", ex3.numeroDomicilios)
locale.setlocale(locale.LC_ALL, 'pt_BR')

x_labels = list(ex3.numeroDomicilios)
x_pos = list(range(0, len(ex3.numeroDomicilios)))
values = [value for key, value in ex3.numeroDomicilios.items()]

plt.ticklabel_format(style = 'plain')
plt.bar(x_pos, values)
plt.xticks(x_pos, x_labels)
plt.ylabel('domicílios')
plt.xlabel('ano')
plt.title('Domicílios/ano')
plt.tick_params(axis='y',labelleft=False, direction='in')

for x, value in zip(x_pos, values):
	plt.text(x, 1.02 * value, "{0:n}".format(value), horizontalalignment='center')

plt.savefig('%s/ex3a.png' % ex3.path)
# plt.show()