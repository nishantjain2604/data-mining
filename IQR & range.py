def IQRange(a,n):
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
    print("Median =",median)
    print("q1=",q1)
    print("q3=", q3)
    IQR = q3-q1
    return IQR
a = []
n = int(input("Enter number of elements : "))
print("enter the data")
for i in range(0, n):
    l = float(input())
    a.append(l)
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            a[i], a[j] = a[j],a[i]
print("sorted array:",a)
print("range=",a[n-1]-a[0])
print("Inter quartile range=",IQRange(a,n))