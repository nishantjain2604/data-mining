import pandas as pd
def manhattan(a,b):
    distance= 0
    for i in range(len(a)):
        distance = distance + abs(a[i]-b[i])
    return distance
def eucladian(a,b):
    x=0
    for i in range (len(a)):
        x= x+ ((a[i])-(b[i]))**2
        y = x**.5
    return y
df=pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)

print("manhattan distance between maths and science=",manhattan(df.Math,df.Science))
print("eucladian distance between maths and science=",eucladian(df.Math,df.Science))
print("manhattan distance between maths and English=",manhattan(df.Math,df.English))
print("eucladian distance between maths and English=",eucladian(df.Math,df.English))