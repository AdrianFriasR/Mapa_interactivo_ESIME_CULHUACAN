from arbol_edificios import ArbolAVL
from lista_doble import ListaDoblementeLigada
from lista_circular import ListaCircular
from edificio import Edificio
from horario import Horario
from grafo_ESIME import GrafoCampus
from ubicacion import detectar_edificio_actual
from navegacion import calcular_ruta_usuario

arbol = ArbolAVL()

edificio_a = Edificio("A", 19.504312, -99.146832)
edificio_b = Edificio("B", 19.504980, -99.147120)
edificio_c = Edificio("C", 19.503900, -99.146200)

arbol.insertar_edificio("A", edificio_a)
arbol.insertar_edificio("B", edificio_b)
arbol.insertar_edificio("C", edificio_c)

grafo = GrafoCampus()

grafo.agregar_camino("A", "B", 100)
grafo.agregar_camino("B", "C", 80)
grafo.agregar_camino("A", "C", 250)


lat_usuario = 19.504350
lon_usuario = -99.146900

resultado = calcular_ruta_usuario(
    lat_usuario,
    lon_usuario,
    arbol,
    grafo
)

if resultado:
    print("Origen:", resultado["origen"])

    if resultado["destino"]:
        print("Destino:", resultado["destino"])
        print("Ruta:", resultado["camino"])
        print("Distancia:", resultado["distancia"])
        print("Clase:", resultado["clase"])
    else:
        print(resultado["mensaje"])



# # Crear edificio
# edificio_a = Edificio("A", 19.504200, -99.146800)

# # Agregar salones
# edificio_a.agregar_salon("1205")
# edificio_a.agregar_salon("1206")

# # Crear horarios
# h1 = Horario("Lunes", "20:30", "22:00", "Estructura de Datos", "3CV15", "Gonzalez")
# h2 = Horario("Miercoles", "20:30", "22:00", "Estructura de Datos", "3CV15", "Gonzalez")

# # Agregar horarios al salon 1205
# salon_1205 = edificio_a.salones.cabeza.dato
# salon_1205.agregar_horario(h1)
# salon_1205.agregar_horario(h2)

# # Mostrar todo
# print(edificio_a)
# edificio_a.mostrar_salones()
# print("Horarios del salon 1205:")
# salon_1205.mostrar_horarios()

# clases_hoy = edificio_a.clases_del_dia("Lunes")
# for salon, horario in clases_hoy:
#     print(salon, horario)

# salon_1205 = edificio_a.buscar_salon("1205")
# clase = salon_1205.clase_actual()
# if clase:
#     print("Clase actual:", clase)

# arbol = ArbolAVL()

# edificio_a = Edificio("A", 19.504200, -99.146800)
# edificio_b = Edificio("B", 19.504300, -99.146700)
# edificio_c = Edificio("C", 19.504400, -99.146600)

# arbol.insertar_edificio("A", edificio_a)
# arbol.insertar_edificio("B", edificio_b)


# grafo = GrafoCampus()

# grafo.agregar_camino("A", "B", 100)
# grafo.agregar_camino("B", "C", 80)
# grafo.agregar_camino("A", "C", 250)
# grafo.agregar_camino("C", "D", 60)

# camino, distancia = grafo.ruta_mas_corta("A", "D")

# print("Camino:", camino)
# print("Distancia total:", str(distancia) + "m")

# # Ejemplo de uso de la función detectar_edificio_actual

# edificios = [edificio_a, edificio_b, edificio_c]

# lat_usuario = 19.504350
# lon_usuario = -99.146900

# edificio, distancia = detectar_edificio_actual(lat_usuario, lon_usuario, edificios)

# print("Estás cerca del edificio:", edificio.nombre)
# print(f"Distancia aproximada: {distancia:.2f} metros")
