import random
from random import randint
bolsa = []
oficio = ['ladrone', 'Mague', 'Barbare']
heroe = {oficio : []}
print("Bienvenido a aventura amateur by charlydersecano")
print()
print("En primer lugar elija usted un oficio para el personaje con el que va a vivir esta aventura, entre Ladrone, Mague o Barbare")
oficio = input('escriba su oficio: ')
while oficio != 'Ladrone' or 'Mague' or 'Barbare':
    print("¿No sabes escribir? Reinicia y elige uno de los tres, que es para hoy")
    print("Game Over")
    oficio = input('escriba su oficio: ')
if (oficio == 'Ladrone'):
    print("Buena elección, el Ladrone, el valiente, el ágil, es el oficio de quienes gustan de moverse entre las sombras")
elif (oficio == 'Mague'):
    print("Curiosa elección, el Mague no es el más fuerte pero es mentalmente increible, además capaz de lanzar hechizos")
elif (oficio == 'Barbare'):
    print("Veo que tienes ganas de dar guerra. El barbare es un personaje fuerte y resistente, pocos le superan")
    # else:
    # print("¿No sabes escribir? Reinicia y elige uno de los tres, que es para hoy")
    # print("Game Over")
    # while oficio != 'Ladrone' or 'Mague' or 'Barbare':
    #     oficio = str(input ("escriba su oficio: "))
    #       print('bien sigamos')
    #AVERIGUAR COMO HACER UN BUCLE PARA REINICIARLO
print()
print("Dime, persona al otra lado del teclado, ¿Cuál será el nombre de su personaje?")
nombre = str(input("escriba su nombre: "))
print(f"Con que {nombre} el {oficio}, mmm buen nombre, me gusta")
print()
print(f"Bien {nombre}, ahora tienes que seleccionar sus puntos de fuerza, agilidad y mente, entre todos debes repartir 15 puntos con un máximo de 12 de un valor y un mínimo de 1")
fuerza = int(input("fuerza: "))
agilidad = int(input("agilidad: "))
mente = int(input("mente: "))
resistencia = int(((fuerza / 2) + 6) * 2) -10
armas = int(((agilidad / 2) + 6) * 2) - 10
magia = int(((mente / 2) + 6) * 2) - 10
persuasion = int((mente / 2) +3)
suerte = int((agilidad / 2) + 3)
vida = int((fuerza / 2) + 3)
print(f"Además {nombre} tendrá otro atributos como resistencia {resistencia} puntos, manejo de armas {armas} puntos, magia {magia} puntos, suerte {suerte} puntos, persuasión {persuasion} puntos y vida {vida} puntos.")
print(vida)
print()
if int(fuerza + agilidad + mente > 15):
    print("Diablos, eso suma más de 15 puntos, me quieres hacer trampas,¿verdad?")
    print("Booooom")
    print("Caes fulminado por un rayo")
    print("Game Over")
#AVERIGUAR COMO CREAR BUCLE PARA INICIAR ESTE
if int(fuerza + agilidad + mente < 15):
    print("No seas torpe, eso no suma quince, tienes menos puntos de lo normal, restaura y suma bien al añadir tus destrezas")
    print("Game Over")
#AVERIGUAR COMO CREAR BUCLES
if int(fuerza + agilidad + mente == 15):
    print(f"Perfecto, ahora te empezaré a contar la aventura de como {nombre} se forjó su destino")
print()
print(f"Nuestro heroe nació en un pequeño pueblo de la comarca. Cuando creció sus padres le dieron todos sus ahorros para que fuera a la capital Granade a estudiar en la famosa escuela de {oficio}.")
print(f"Se alojó en una habitación en un humilde hospedería para estudiantes conocida como El bartolo. Allí hizo un grupo de amigos y rápidamente se empezaron a llamar de unos a otros de forma familiar. Estaban Mohon, Vali, Txerra, Batos, Kaños, Vivi, Jabal y Moromir, a tí te empezaron a llamar {nombre} y te gustó")
print()

