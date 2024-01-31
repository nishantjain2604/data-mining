print("\n")
import pandas as pd
import numpy as np
df=pd.read_csv(r"F:\M.tech\2nd sem\data\GK.csv")
df.Age.fillna(df.Age.median(),inplace=True)
df.Appearances.fillna(0,inplace=True)
df=df.rename(columns={"Clean sheets":"CS","Goals conceded":"GC","Errors leading to goal":"Errors","Penalties saved":"PS"})
df.CS.fillna(0,inplace=True)
df.GC.fillna(0,inplace=True)
df.Errors.fillna(0,inplace=True)
df.Saves.fillna(0,inplace=True)
df.PS.fillna(df.PS.mean(),inplace=True)
df = df.dropna(axis=1)
detail = dict(zip(df['Name'], df['Appearances']))
q1=np.percentile(df.Appearances,25)
q3=np.percentile(df.Appearances,75)
iqr=q3-q1
upper_fence = q3+1.5*iqr
lower_fense = q1-1.5*iqr
print("outliers=")
for i in range (len(df.Saves)):
    if df.Appearances[i]<lower_fense:
        print(f"Name: {df['Name'][i]}, Appearances: {df['Appearances'][i]}")
    elif df.Appearances[i]>upper_fence:
        print(f"Name: {df['Name'][i]}, Appearances: {df['Appearances'][i]}")
    else:
        continue
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(x=df['Appearances'])
plt.show()