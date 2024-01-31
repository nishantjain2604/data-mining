import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
Math=df.Math
English=df.English
Science=df.Science
Geography=df.Geography
DS=[Math,English,Science,Geography]

figure = plt.figure(figsize =(10, 7))
ax = figure.add_subplot(111)
bp = ax.boxplot(DS, patch_artist = True,notch ='True', vert = 0)
colors = ['#00FF00','#0F00FF', '#F00FF0','#FFFF0F']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
for whisker in bp['whiskers']:
    whisker.set(color ='#8E008B',linewidth = 1.4,linestyle =":")
for cap in bp['caps']:
    cap.set(color ='#8E008B',linewidth = 2.1)
for median in bp['medians']:
    median.set(color ='blue',linewidth = 3)
for flier in bp['fliers']:
    flier.set(marker ='D',color ='#d7298c',alpha = 0.6)
ax.set_yticklabels(['math', 'english','science', 'geography'])
plt.title("Customized box plot using attributes")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.show()