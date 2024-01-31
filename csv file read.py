import numpy as np
import pandas as pd
df = pd.read_csv(r"F:/M.tech/2nd sem/data/harshit.csv",)
def mean(x):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + x[i]
    m = sum / len(x)
    return m
def med(a):
    n=len(a)
    for i in range (0,len(a)):
        for j in range (i+1,len(a)):
            if a[i]>a[j]:
                a[i], a[j] = a[j],a[i]
    if n%2==0:
        x=n//2
        median=(a[x-1]+a[x])/2
    else:
        median = a[((n+1)//2)-1]
    return median
def mode(a):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    l1 = []
    i = 0
    while i<len(a):
        l1.append(a.count(a[i]))
        i+=1
    d1 = dict(zip(a, l1))
    d2 = {k for (k, v) in d1.items() if v == max(l1)}
    return d2
def IQRange(a):
    a.sort()
    n=len(a)
    if n%2==0:
        x=n//2
        median=(a[x-1]+a[x])/2
        q= ((x+1)//2)-1
        q1= a[q]
        q3= a[x+q]
    else:
        x= (n+1)//2-1
        median = a[x]
        y1 = []
        for i in range (0,x):
            y1.append(a[i])
        q1 = y1[len(y1)//2]
        y2 = []
        for i in range (x+1,n):
            y2.append(a[i])
        q3 = y2[len(y2)//2]
    IQR = q3-q1
    return IQR
def SD(a):
    m= mean(a)
    x = 0
    for i in range(len(a)):
        x = x + (a[i] - m) ** 2
    Std_Dev = (x / len(a)) ** .5
    return Std_Dev
english = []
for i in range(0, len(df.English)):
    english.append(df.English[i])
Science =[]
for i in range(0, len(df.Science)):
    Science.append(df.Science[i])
print("mean of math=",mean(df.Math))
print("mode of science=",mode(Science))
print("iqr of english",IQRange(Science))
print("Std deviation of Geography=",SD(df.Geography))
print("median of english=",med(english))
