from random import randint

check = 0

# Funcion para comparar si una variable dentro de un diccionario es mas grande que una variable dada
def comparacion_mas_que(lista, cant, variable):
    lista_true = []
    for equipo in lista:
        if equipo[variable] > cant:
            lista_true.append(equipo)
    return lista_true

# Funcion para comparar si una variable dentro de un diccionario es mas pequeña que una variable dada
def comparacion_menos_que(lista, cant, variable):
    lista_true = []
    for equipo in lista:
        if equipo[variable] < cant:
            lista_true.append(equipo)
    return lista_true

# Funcion para comparar si una variable dentro de un diccionario es igual que una variable dada
def comparacion_igual(lista, cant, variable):
    lista_true = []
    for equipo in lista:
        if equipo[variable] == cant:
            lista_true.append(equipo)
    return lista_true

# Funcion para comparar si una variable dentro de un diccionario no es igual a una variable dada
def comparacion_not_igual(lista, cant, variable):
    lista_true = []
    for equipo in lista:
        if equipo[variable] != cant:
            lista_true.append(equipo)
    return lista_true

# Funcion para obtener todas las variables de un item en un diccionario
def get_all_possibilities(lista, variable):
    list_return = []
    for equipo in lista:
        list_return.append(equipo[variable])
    return list_return

# Funcion para obtener la mejor opcion para preguntar dentro de una lista de posibilidades (string)
def best_option(posibilities):
    best_item = 0
    for item in posibilities:
        var = posibilities.count(item)
        if best_item < var:
            if best_item == 2:
                best_item = var - randint(0, 1)
            else:
                best_item = var - 1
    return posibilities[best_item]

# Funcion para obtener la mejor opcion para preguntar dentro de una lista de posibilidades (int)
def best_option_number(posibilities):
    total = 0
    for item in posibilities:
        total = total + item
    best_item = total // len(posibilities)
    return best_item

# Funcion para obtener la mejor pregunta posible para eliminar la mitad de las opciones de una lista
def get_best_question(list):
    PREGUNTA_1 = {"Question": "¿El equipo ha ganado la Copa Libertadores? ",
                  "Function": comparacion_mas_que(list, 0, "Libertadores")}

    PREGUNTA_2 = {"Question": "¿El equipo ha ganado algún título local? ",
                  "Function": comparacion_mas_que(list, 0, "Titulos_Locales")}

    PREGUNTA_3 = {"Question": "¿El equipo ha ganado algún título internacional? ",
                  "Function": comparacion_mas_que(list, 0, "Titulos_Internacionales")}

    PREGUNTA_4 = {"Question": "¿Su equipo está entre los cuatro grandes? ",
                  "Function": comparacion_igual(list, True, "Cuatro_Grandes")}

    PREGUNTA_5 = {"Question": "¿Su equipo tiene el color {}? ".format(*best_option(get_all_possibilities(list, "Color"))),
                  "Function": comparacion_igual(list, best_option(get_all_possibilities(list, "Color")), "Color")}

    PREGUNTA_6 = {"Question": "¿La marca de camiseta de su equipo es {}? ".format(
        best_option(get_all_possibilities(list, "Marca"))),
                  "Function": comparacion_igual(list, best_option(get_all_possibilities(list, "Marca")), "Marca")}

    PREGUNTA_7 = {"Question": "¿El rival de su equipo juega en Primera División? ",
                  "Function": comparacion_not_igual(list, False, "Rival")}

    PREGUNTA_8 = {"Question": "¿El apodo de su equipo es {}? ".format(best_option(get_all_possibilities(list, "Apodo"))),
                  "Function": comparacion_igual(list, best_option(get_all_possibilities(list, "Apodo")), "Apodo")}

    PREGUNTA_9 = {"Question": "¿Su equipo tiene mas de {} titulos locales? ".format(
        best_option_number(get_all_possibilities(list, "Titulos_Locales"))),
                  "Function": comparacion_mas_que(list,
                                                  best_option_number(get_all_possibilities(list, "Titulos_Locales")),
                                                  "Titulos_Locales")}

    PREGUNTA_10 = {"Question": "¿Su equipo tiene mas de {} titulos internacionales? ".format(
        best_option_number(get_all_possibilities(list, "Titulos_Internacionales"))),
                   "Function": comparacion_mas_que(list, best_option_number(
                       get_all_possibilities(list, "Titulos_Internacionales")), "Titulos_Internacionales")}

    PREGUNTA_11 = {"Question": "¿Su equipo ha descendido de primera división dos veces o más? ",
                   "Function": comparacion_mas_que(list, 1, "Descensos")}

    PREGUNTA_12 = {}

    all_questions = [PREGUNTA_1, PREGUNTA_2, PREGUNTA_3, PREGUNTA_4, PREGUNTA_5, PREGUNTA_6, PREGUNTA_7, PREGUNTA_8,
                     PREGUNTA_9, PREGUNTA_10, PREGUNTA_11]

    CONST = len(list) // 2
    best_number = 999999
    best_question = None
    for question in all_questions:
        if abs((len(question["Function"]) - CONST)) < abs((best_number - CONST)):
            best_number = len(question["Function"])
            best_question = question
        if abs((len(question["Function"]) - CONST)) == abs((best_number - CONST)):
            check = randint(0, 1)
            if check == 1:
                best_number = len(question["Function"])
                best_question = question
    return best_question

# Funcion para obtener una pregunta de un diccionario y validar la respuesta del usuario
def get_respuesta(question):
    response = input(question['Question'])
    while response != "SI" and response != "si" and response != "no" and response != "NO":
        print("Por favor introducir SI o NO")
        response = input(question['Question'])
    return response

# Funcion para devolver una lista de elementos de un diccionario en base a la respuesta del usuario
def respuesta_pregunta(question):
    return question['Function']
