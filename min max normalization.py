def normalization(a):
    new = []
    for i in range (n):
        x= (a[i]-a[0])/(a[n-1]-a[0])
        new.append(x)
    return new
a = []
n = int(input("Enter number of elements : "))
print("enter the data")
for i in range(0, n):
    l = float(input())
    a.append(l)
a.sort()
print("soted array", a)
print("min max normalization",normalization(a))