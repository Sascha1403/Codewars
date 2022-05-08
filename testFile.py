import math

a = [1,7,6,10,21,5,9,8,5,4]

subset = [[a[i],a [j]] for i in range(len(a)) for j in range(i+1, len(a))]
test = [math.prod(subset[i]) for i in range(len(subset))]
res = sum(test)

print(subset)
print(test)
print(res)
