import pandas as pd
from sklearn.decomposition import PCA
df=pd.read_csv(r"F:\M.tech\2nd sem\data\GK.csv")
df= df.drop(['Club','Nationality','Name'],axis=1)
df.Age.fillna(df.Age.median(),inplace=True)
df.Appearances.fillna(0,inplace=True)
df=df.rename(columns={"Clean sheets":"CS","Goals conceded":"GC","Errors leading to goal":"Errors","Penalties saved":"PS"})
df.CS.fillna(0,inplace=True)
df.GC.fillna(0,inplace=True)
df.Errors.fillna(0,inplace=True)
df.Saves.fillna(0,inplace=True)
df.PS.fillna(df.PS.mean(),inplace=True)
df = df.dropna(axis=1)
print("\n")
pca = PCA(n_components = 3)
pca.fit(df)
PCA(copy=True, n_components=3, whiten=False)
df1 = pca.transform(df)
df_2d = pd.DataFrame(df1)
df_2d.index = df.index
df_2d.columns = ['PC1','PC2','PC3']
print(df_2d.head(45))