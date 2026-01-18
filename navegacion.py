from ubicacion import detectar_edificio_actual
from planificador import detectar_edificio_destino


def calcular_ruta_usuario(lat, lon, arbol_edificios, grafo):


    # Estructura base del resultado (API estable)
    resultado = {
        "origen": None,
        "destino": None,
        "camino": [],
        "distancia": None,
        "clase": None,
        "mensaje": None
    }

    # 1. Obtener edificios desde el AVL (ordenados)
    edificios = arbol_edificios.inorden()

    if not edificios:
        resultado["mensaje"] = "No hay edificios registrados"
        return resultado

    # 2. Detectar edificio de origen por GPS
    edificio_origen, dist_origen = detectar_edificio_actual(
        lat, lon, edificios
    )

    if edificio_origen is None:
        resultado["mensaje"] = "No se pudo detectar el edificio actual"
        return resultado

    resultado["origen"] = edificio_origen.nombre

    # 3. Detectar edificio destino según horario
    edificio_destino, clase = detectar_edificio_destino(arbol_edificios)

    if edificio_destino is None:
        resultado["mensaje"] = "No tienes clase en este momento"
        return resultado

    resultado["destino"] = edificio_destino.nombre
    resultado["clase"] = clase

    # 4. Calcular ruta más corta con el grafo
    camino, distancia = grafo.ruta_mas_corta(
        edificio_origen.nombre,
        edificio_destino.nombre
    )

    if not camino:
        resultado["mensaje"] = "No se encontró una ruta disponible"
        return resultado

    resultado["camino"] = camino
    resultado["distancia"] = distancia

    return resultado
