a = ['oi', 'ola', 'eu', 'vc']

print('Lista "a": {}'.format(a))

# assim vc printa a possição do nome q escolher

ex1 = a[2]
ex2 = a.index('eu')

print('possição da palavra "{}" na lista "a": {}'.format(ex1, ex2))

# assim vc add em ultimo
a.append('nic')
print('adicionando "nic" a ultima posição da lista "a": ' + str(a))

# assim vc add onde quiser
a.insert(0, 'jao')
print('adicionando "jao" na primeira posição da lista "a": ' + str(a))

# isso esta errado
# a = a.append('algo')

# tbm não funciona, pq 'b' não é uma lista
# b = 'oi'
# b.append('ola')

# assim vc remove pelo nome
a.remove('eu')
print('removendo "eu" da lista "a": ' + str(a))

# assim vc remove pela posição
del a[1]
print('removendo a palavra na posição "1" da lista "a": ' + str(a))

print('\n\n\n')

b = [5, 6, 84, -5, 1, -65, 78, 125]

print('Lista "b": ' + str(b))

b.sort()
print('organizando a lista "b" em ordem crescente: ' + str(b))

# esta errado
# print(b.sort())

b.sort(reverse=True)
print('organizando a lista "b" em ordem decrescente: ' + str(b))

print('\n\n\n')

c = ['a', 'z', 'c', 'b', 'd', 'y']

print('Lista "c": ' + str(c))

c.sort()
print('organizando a lista "c" em ordem alfabetica: ' + str(c))

c.sort(reverse=True)
print('organizando a lista "c" em ordem alfabetica oposta: ' + str(c))

print('\n\n\n')

# lista com int e str.
x = [1, 2, 3, 'jao', 'nic']

# isso não funciona pq o Python não sabe organizar int e str.
# d.sort()

# mas isso funciona, pq é td str.
d = ['2', 'jao', '3', '1', 'nic']

print('Lista "d": ' + str(d))

d.sort()
print('organizando a lista "d" em ordem crescente e alfabetica: ' + str(d))

print('\n\n\n')

e = ['a', 'B', 'A', 'z', 'b', 'Z']

print('Lista "e": ' + str(e))

# ordem ASCII
e.sort()
print('organizandoa lista "e" em ordem alfabetica e com as maiusculas primeiro: ' + str(e))

# ordem alfabetica
e.sort(key=str.lower)
print('organizandoa lista "e" em ordem alfabetica ignorando as maiusculas: ' + str(e))
