import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
Math=df.Math
English=df.English
Science=df.Science
Geography=df.Geography
History=df.History
DS=[Math,English,Science,Geography,History]
figure = plt.figure(figsize =(10, 7))
figure, ax = plt.subplots()
bp = ax.boxplot(DS)
ax.set_xticklabels(['math', 'english','science', 'geography','History'])
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.show()