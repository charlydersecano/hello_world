#LISTAS

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

#TUPLAS

tupla = (1, 'perro', 'rio', True)
print(tupla[2])

print(tupla.index('rio'))
print(tupla.count(True))
print(tupla.count('perro'))

#SETS
animales_del_zoo ={'cuervos', 'leones', 'monos', 'monos', 'tigres', 'elefantes', 'tigres', 'flamencos', 'monos', 'hipopotamos', 'monos'}
print(animales_del_zoo)
animales_silvestres={'monos', 'javalies', 'ciervos', 'osos', 'hipopotamos', 'linces', 'armadillos', 'osos', 'tigres'}
comunes = animales_del_zoo.intersection(animales_silvestres)
print(comunes)
print(animales_del_zoo - animales_silvestres)

los_otros = animales_del_zoo.difference(animales_silvestres)
print(los_otros)

set_tupla = set(tupla)

#Diccionarios
yo = {'nombre' : 'Carlos',
      'sexo' : 'hombre',
      'edad' : 37,
      'job' : 'tester',
      'hermanos' : 1,
      'simpatico' : True,
      'deportista' : False,
      'altura' : 1.81,
      'peso' : 73.5,
      'gustos': ['leer', 'viajar', 'naturaleza']}

