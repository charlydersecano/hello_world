#Fruteria
cosas = ['platanos', 'manzanas', 'huevos', 'panes', 'yogur']
cantidad = [7,            8,         12,        3,        6]

#establecemos reservas
platanico = cosas.index('platanos')
manzanica = cosas.index('manzanas')
huevin = cosas.index('huevos')
panecillo = cosas.index('panes')
yogurcin = cosas.index('yogur')

#Abren la tienda y cola de clientes
print('Buenos días, tenemos', cosas)

#COMPRAS

print('quiero un platano y dos yogures')
cantidad[platanico] = cantidad[platanico] - 1
cantidad[yogurcin] = cantidad[yogurcin] - 2

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[panecillo] < 1:
    print('ya no quedan panes')
    cosas.remove('panes')
else:
    print(f'Aun quedan', cantidad[panecillo], 'panes')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')
print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 4 manzanas y media docena de huevos')
cantidad[manzanica] = cantidad[manzanica] - 4
cantidad[huevin] = cantidad[huevin] - 6

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[panecillo] < 1:
    print('ya no quedan panes')
    cosas.remove('panes')
else:
    print(f'Aun quedan', cantidad[panecillo], 'panes')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 2 manzanas y 1 barra de pan')
cantidad[manzanica] = cantidad[manzanica] - 2
cantidad[panecillo] = cantidad[panecillo] - 1

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[panecillo] < 1:
    print('ya no quedan panes')
    cosas.remove('panes')
else:
    print(f'Aun quedan', cantidad[panecillo], 'panes')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 3 platanos y 1 barra de pan')
cantidad[platanico] = cantidad[platanico] - 3
cantidad[panecillo] = cantidad[panecillo] - 1

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[panecillo] < 1:
    print('ya no quedan panes')
    cosas.remove('panes')
else:
    print(f'Aun quedan', cantidad[panecillo], 'panes')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 2 yogures y 1 barra de pan')
cantidad[yogurcin] = cantidad[yogurcin] - 2
cantidad[panecillo] = cantidad[panecillo] - 1

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[panecillo] < 1:
    print('ya no quedan panes')
    cosas.remove('panes')
else:
    print(f'Aun quedan', cantidad[panecillo], 'panes')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 1 platano y media docena de huevos')
cantidad[platanico] = cantidad[platanico] - 1
cantidad[huevin] = cantidad[huevin] - 6

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[huevin] < 1:
    print('ya no quedan huevos')
    cosas.remove('huevos')
else:
    print(f'Aun quedan', cantidad[huevin], 'huevos')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('quiero 2 yogures y dos manzanas')
cantidad[yogurcin] = cantidad[yogurcin] - 2
cantidad[manzanica] = cantidad[manzanica] - 2

if cantidad[platanico] < 1:
    print('ya no quedan platanos')
    cosas.remove('platanos')
else:
    print(f'Aun quedan', cantidad[platanico], 'platanos')
if cantidad[manzanica] < 1:
    print('ya no quedan manzanas')
    cosas.remove('manzanas')
else:
    print(f'Aun quedan', cantidad[manzanica], 'manzanas')
if cantidad[yogurcin] < 1:
    print('ya no quedan yogures')
    cosas.remove('yogur')
else:
    print(f'Aun quedan', cantidad[yogurcin], 'yogures')

print('Buenos días ¿Que les queda?')
print('Buenos días, tenemos', cosas)
print('Entonces no quiero nada')
print('Pues mejor nos comemos los platanos y abrimos mañana.')