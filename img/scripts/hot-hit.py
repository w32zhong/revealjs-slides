import math
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

with open('./hot-hit.stats') as f:
    for line in f:
        line = line.strip('\n')
        fields = line.split()
        print(fields)
        hits = int(fields[0])
        freq = math.log(int(fields[3]))
        x.append(hits)
        y.append(freq)

label1 = 'log(freq)'
label2 = 'number of hit paths'

# create plot
fig, (ax2, ax1) = plt.subplots(1, 2)
bar_width = 0.8
indices = np.arange(len(x)) + bar_width

ax1.barh(indices, y, bar_width, color='grey', hatch=" ")
ax1.set_xlabel(label1)
ax1.set_ylabel(label2)

y_sticks = [_ for i, _ in enumerate(indices) if i % 4 == 0]
y_sticks_labels = [_ for i, _ in enumerate(x) if i % 4 == 0]

ax1.set_yticks(y_sticks)
ax1.set_yticklabels(y_sticks_labels)
ax1.set_ylim([0, 60])

w, h =(7, 4.5)
fig.set_size_inches(w, h)

###########################################################

x = []
y = []

with open('./qry-len.stats') as f:
    for idx, line in enumerate(f):
        line = line.strip('\n')
        fields = line.split()
        print(fields)
        l = int(fields[0])
        x.append(idx + 1)
        y.append(l)

label1 = 'query length'
label2 = 'query ID'

# create plot
index = np.arange(len(x))
bar_width = 0.8
indices = index + bar_width

ax2.barh(indices, y, bar_width, color='grey', hatch=" ")
ax2.set_xlabel(label1)
ax2.set_ylabel(label2)

y_sticks = [_ for i, _ in enumerate(indices) if i % 1 == 0]
y_sticks_labels = [_ for i, _ in enumerate(x) if i % 1 == 0]

ax2.set_yticks(y_sticks)
ax2.set_yticklabels(y_sticks_labels)
ax2.set_ylim([0, 21])

w, h =(7, 4.5)
fig.set_size_inches(w, h)

plt.tight_layout()
plt.show()
fig.savefig('./hot-hit.svg')
plt.close(fig)
