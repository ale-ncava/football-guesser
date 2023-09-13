from utils.consts import PRIMERA_NACIONAL
from utils.functions import *

flag = False
lista_send = PRIMERA_NACIONAL

#Inicio de Programa
while not flag:
    pregunta = get_best_question(lista_send)
    respuesta = get_respuesta(pregunta)
    if respuesta == "SI" or respuesta == "si":
        lista_send = respuesta_pregunta(pregunta)
    elif respuesta == "NO" or respuesta == "no":
        lista_rest = respuesta_pregunta(pregunta)
        for item in lista_rest:
            lista_send.remove(item)
    if len(lista_send) == 1:
        final = lista_send[0]
        print("El equipo en el que estás pensando es: {}".format(final['Equipo']))
        flag = True
