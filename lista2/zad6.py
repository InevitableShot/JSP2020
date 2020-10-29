list = ['Kasia', 'Basia', 'Marek', 'Darek']
list.append('Józek')
print(list)
list.extend(['Ania', 'Basia'])
print(list)
list.sort()
print(list)
print(list[3])
print(list[:2])
print(list[-2:])
i = 0
while i < (len(list)-1):
    if list[i] == 'Basia':
        list.remove(list[i])
    else:
        i += 1
print(list)
print(len(list))
print(tuple(list))