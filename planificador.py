from datetime import datetime

# Funciones para obtener la fecha y hora actual
def obtener_dia_actual():
    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miercoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sabado",
        6: "Domingo"
    }
    hoy = datetime.now().weekday()
    return dias[hoy]


def obtener_hora_actual():
    return datetime.now().strftime("%H:%M")


# Funcion para comparar por horas

def hora_en_rango(hora_actual, hora_inicio, hora_fin):
    return hora_inicio <= hora_actual <= hora_fin

# Detectar el edificio destino segun el horario

def detectar_edificio_destino(arbol_edificios):
    dia = obtener_dia_actual()
    hora = obtener_hora_actual()

    edificios = arbol_edificios.inorden()

    for edificio in edificios:
        clases = edificio.clases_del_dia(dia)

        for salon_numero, horario in clases:
            if hora_en_rango(hora, horario.hora_inicio, horario.hora_fin):
                return edificio, horario

    return None, None
