from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

import numpy as np
from pylab import *

name=str(sys.argv[1])

d=[]

distance_file = open('../yaml/' + name + '.txt')

d.append(np.absolute(map(double, distance_file.readlines())))

means = mean(d)

n=np.arange(0,len(d[0]),1)

# plot it
fig = plt.figure(figsize=(10, 4))
ax0 = plt.subplot2grid((1, 10), (0, 0), colspan=8)
axes = plt.gca()
#axes.set_ylim([0,1.5])
ax0.plot(n, d[0])
plt.ylabel('Positionsfehler in Meter')
plt.xlabel('Zeit in Sekunden')
ax1 = plt.subplot2grid((1, 10), (0, 8), colspan=2)
axes = plt.gca()
#axes.set_ylim([0,1.5])
ax1.yaxis.tick_right()
bp_dict = ax1.boxplot(d, whis=np.inf)
ax1.scatter(1,means,marker="_",color='g',linewidths=1,s=200)
for line in bp_dict['medians']:
    x, y = line.get_xydata()[1]
    text(x+0.02, y, '%.2f' % y, verticalalignment='center',color='red')
for line in bp_dict['boxes']:
    x, y = line.get_xydata()[3]
    text(x-0.02, means, '%.2f' % means, verticalalignment='center', horizontalalignment='right',color='green')
line = bp_dict['caps'][0]
x, y = line.get_xydata()[1]
text(x+0.02, y, '%.2f' % y, verticalalignment='center', horizontalalignment='left',color='black')



plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')

fig.savefig('../vis/' + name +'.pdf')
plt.show()
