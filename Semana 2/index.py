x = int(input())

l = [1]
for cont in range(1, 50):
    l.append(l[-1]*(x/cont))

print(sum(l))
