#Fruteria
cosas = ['platanos', 'manzanas', 'huevos', 'pan', 'yogur']
cantidad = [7,            8,         12,        1,        6]

#establecemos reservas
platanico = cosas.index('platanos')
manzanica = cosas.index('manzanas')
huevin = cosas.index('huevos')
panecillo = cosas.index('pan')
yogurcin = cosas.index('yogur')



#COMPRAs

#quiero un platano y un huevo
cantidad[platanico] = cantidad[platanico] - 1
cantidad[huevin] = cantidad[huevin] - 1

#quiero 4 manzanas y media docena de huevos
cantidad[manzanica] = cantidad[manzanica] - 4
cantidad[huevin] = cantidad[huevin] - 6

if cantidad[platanico] = 0:
    print('ya no quedan platanos')
    cosas.remove('platanos')
    else:
print(f'Aun nos queda', cosas)








