import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d = pd.read_csv('full_python_3_notebook_data.csv')
depth = d['MaxDepth']

bins = np.arange(0,7,1)

fig, ax = plt.subplots(figsize=(9, 5))

_, bins, patches = plt.hist([np.clip(depth, bins[0], bins[-1])],
##                                density=True,
                                bins=bins, color=['pink'], rwidth=0.7)
##plt.hist([loops], color=['teal'], bins=bins, rwidth=0.5,normed=1)

xlabels = bins.astype(str)
xlabels[-2] += '+'
xlabels[-1] = ''

N_labels = len(xlabels)
plt.xlim([0, 6])
plt.xticks(1 * np.arange(N_labels)+0.5, fontsize=16 )
ax.set_xticklabels(xlabels)

ax.yaxis.set_tick_params(labelsize=16) 

# Phil's suggestion - 2nd y axis on right with percentages
ax2 = ax.twinx()
mn, mx = ax.get_ylim()
ax2.set_ylim(mn*(100/len(depth)), mx*(100/len(depth)))
ax2.set_ylabel('percent', fontsize=16) 
ax2.yaxis.set_tick_params(labelsize=16) 


ax.set_xlabel('maximum for loop nesting depth in notebook', fontsize=16)
ax.set_ylabel('notebooks', fontsize=16)

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
