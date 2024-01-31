x = [9,8,5,9,6,4,8,3,7,5,9]
def mode(a):
    a.sort()
    print("sorted array",a)
    l1 = []
    i = 0
    while i<len(a):
        l1.append(a.count(a[i]))
        i+=1
    d1 = dict(zip(a, l1))
    d2 = {k for (k, v) in d1.items() if v == max(l1)}
    return d2
print("mode=",mode(x))