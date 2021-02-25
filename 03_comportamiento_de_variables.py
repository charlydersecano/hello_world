#Arca de Noe
arca = [{'animal': 'leones', 'cantidad': 0},
        {'animal': 'cerdos', 'cantidad': 4},
        {'animal': 'gacelas', 'cantidad': 1},
        {'animal': 'cebras', 'cantidad': 3},
        {'animal': 'cocodrilos', 'cantidad': 3},
        {'animal': 'perros', 'cantidad': 2}]

leon = arca[0]['animal']
cantidadleones = arca[0]['cantidad']
cerdo = arca[1]['animal']
cantidadcerdos = arca[1]['cantidad']
gacela = arca[2]['animal']
cantidadgacelas = arca[2]['cantidad']
cebra = arca[3]['animal']
cantidadcebras = arca[3]['cantidad']
cocodrilo = arca[4]['animal']
cantidadcocodrilos = arca[4]['cantidad']
perro = arca[5]['animal']
cantidadperros = arca[5]['cantidad']

print(arca)

print('traen un leon')
arca[0]['cantidad'] = cantidadleones +1
print('traen tres gacelas')
arca[2]['cantidad'] = cantidadgacelas + 3
print('un cocodrilo mata a otro')
arca[4]['cantidad'] = cantidadcocodrilos -1
print('una cerda pare tres cerditos')
arca[2]['cantidad'] = cantidadcerdos + 3
print('se escapan dos cebras')
arca[3]['cantidad'] = cantidadcebras - 2
print('un perrito escapado vuelve sólo')
arca[5]['cantidad'] = cantidadperros + 1

print(arca)