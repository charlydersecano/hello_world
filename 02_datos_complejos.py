lista_de_la_compra = ['platanos', 'manzanas']
print('lista_de_la_compra', lista_de_la_compra)

print(lista_de_la_compra[0])

lista_de_la_compra.append('chocolate')
lista_de_la_compra.append('gato')
lista_de_la_compra.append('tortuga')
lista_de_la_compra.append('gato')

print(lista_de_la_compra.count('gato'))

print(lista_de_la_compra)
lista_de_la_compra[2] = 'anarcardos'
print(lista_de_la_compra)

print(len(lista_de_la_compra))

lista_de_la_compra.pop()
print(lista_de_la_compra)
borrado = lista_de_la_compra.pop(3)
print(lista_de_la_compra)
print('el ultimo borrado es', borrado)

lista_de_la_compra.remove('tortuga')
print(lista_de_la_compra)

lista_de_la_compra.append('tomates')
print(lista_de_la_compra)

print(lista_de_la_compra[2])
print(lista_de_la_compra[3])

print(lista_de_la_compra[0:2])

lista_de_la_compra[1] = 'peras'
print(lista_de_la_compra)








