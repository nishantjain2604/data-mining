a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    l = float(input())
    a.append(l)
def med(a):
    for i in range (0,len(a)):
        for j in range (i+1,len(a)):
            if a[i]>a[j]:
                a[i], a[j] = a[j],a[i]
    print("sorted array:",a)
    if n%2==0:
        x=n//2
        median=(a[x-1]+a[x])/2
    else:
        median = a[((n+1)//2)-1]
    return median
print("median=",med(a))