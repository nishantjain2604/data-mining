import pandas as pd
import numpy as np
import statistics as st
def normalization(a):
    new = []
    n=len(a)
    x=min(a)
    y=max(a)
    for i in range (n):
        z= round((a[i]-x)/(y-x),2)
        new.append(z)
    return new
def z_score(a):
    m= st.mean(a)
    sd= st.stdev(a)
    new=[]
    for i in range(len(a)):
        new.append((a[i]-m)/sd)
    return new
df=pd.read_csv(r"F:\M.tech\2nd sem\data\GK.csv")
#df= df.drop(['Club','Nationality','Name'],axis=1)
df.Age.fillna(df.Age.median(),inplace=True)
df.Appearances.fillna(0,inplace=True)
df=df.rename(columns={"Clean sheets":"CS","Goals conceded":"GC","Errors leading to goal":"Errors","Penalties saved":"PS"})
df.CS.fillna(0,inplace=True)
df.GC.fillna(0,inplace=True)
df.Errors.fillna(0,inplace=True)
df.Saves.fillna(0,inplace=True)
df.PS.fillna(df.PS.mean(),inplace=True)
df = df.dropna(axis=1)
df.Age = normalization(df.Age)
df.Saves=z_score(df.Saves)
print('\n')
print(" Age   Appearances")
for i in range (len(df.Saves)):
        print(f" {df['Age'][i]}, {df['Appearances'][i]}")
