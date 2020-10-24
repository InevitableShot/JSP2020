l = []
for x in range(0, 100, 3):
    l.append(x)
print(l)
del(l[4:len(l):3])
print(l)
print(sum(l)/len(l))