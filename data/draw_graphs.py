import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d = pd.read_csv('full_python_3_notebook_data.csv')
loops = d['ForLoops']
depth = d['MaxDepth']

bins = np.arange(0,22,1)

fig, ax = plt.subplots(figsize=(9, 5))

_, bins, patches = plt.hist([np.clip(loops, bins[0], bins[-1])],
##                                density=True,
                                bins=bins, color=['teal'], rwidth=0.7)
##plt.hist([loops], color=['teal'], bins=bins, rwidth=0.5,normed=1)

xlabels = bins.astype(str)
xlabels[-2] += '+'
xlabels[-1] = ''

N_labels = len(xlabels)
plt.xlim([0, 20])
plt.xticks(1 * np.arange(N_labels)+0.5)
ax.set_xticklabels(xlabels)

# Phil's suggestion - 2nd y axis on right with percentages
ax2 = ax.twinx()
mn, mx = ax.get_ylim()
ax2.set_ylim(mn*(100/len(loops)), mx*(100/len(loops)))
ax2.set_ylabel('percent', fontsize='x-large')

ax.set_xlabel('number of for loops in notebook', fontsize='x-large')
ax.set_ylabel('notebooks', fontsize='x-large')

#plt.yticks([])
#plt.title('')
#plt.setp(patches, linewidth=0)
#plt.legend(loc='upper left')

fig.tight_layout()


#xlabels = np.array(bins[1:], dtype='|S4')
#xlabels[-1] = '20+'

#N_labels = len(xlabels)
#plt.xticks(np.arange(N_labels), xlabels)


plt.show()
