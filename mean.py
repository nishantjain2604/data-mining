def mean(x):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + x[i]
    m = sum / len(x)
    return m
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    l = float(input())
    a.append(l)
print("\n mean=",mean(a))
