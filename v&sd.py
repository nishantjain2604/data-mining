def read():
    a = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        l = float(input())
        a.append(l)
    return a
def mean(x):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + x[i]
    m = sum / len(x)
    return m
def SD(a):
    m= mean(a)
    x = 0
    for i in range(len(a)):
        x = x + (a[i] - m) ** 2
    Std_Dev = (x / len(a)) ** .5
    return Std_Dev
y = read()
print("Variance=",SD(y)**2)
print("std_deviation=",SD(y))
