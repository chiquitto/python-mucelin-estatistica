import ex3
from matplotlib import pyplot as plt
import locale
import sys

print("dados:", ex3.numeroDomicilios)
locale.setlocale(locale.LC_ALL, 'pt_BR')

x_labels = list(ex3.numeroDomicilios)
x_pos = list(range(0, len(ex3.numeroDomicilios)))
values = [value for key, value in ex3.numeroDomicilios.items()]

print("x_labels: ", x_labels)
print("x_pos: ", x_pos)
print("values: ", values)

# plt.ticklabel_format(style = 'plain')
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))
ax.ticklabel_format(style = 'plain')

for label, pos, value in zip(x_labels, x_pos, values):
	print("label: ", label)
	print("pos: ", pos)
	print("value: ", value)

	label = "{0:n} ({1:n})".format(label, value)
	ax.scatter(pos, value, label=label)

plt.xticks(x_pos, x_labels)
plt.ylabel('domicílios')
plt.xlabel('ano')
plt.title('Domicílios/ano')
plt.tick_params(axis='y',labelleft=False, direction='in')
plt.tick_params(axis='y',labeltop=False, direction='in')
# plt.tick_params(axis='x',labelbottom=False, direction='in')

plt.legend(loc='upper left')

# for x, value in zip(x_pos, values):
# 	if x == 3:
# 		plt.text(x - .1, value * .99, "{0:n}".format(value), horizontalalignment='right')
# 	else:
# 		plt.text(x + .1, value, "{0:n}".format(value), horizontalalignment='left')

plt.savefig('%s/ex3c.png' % ex3.path)
# plt.show()