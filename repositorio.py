from arbol_edificios import ArbolAVL
from grafo_ESIME import GrafoCampus
from edificio import Edificio
from models import EdificioDB, CaminoDB


def cargar_sistema():
    arbol = ArbolAVL()
    grafo = GrafoCampus()

    edificios = EdificioDB.query.all()
    for e in edificios:
        edificio = Edificio(e.nombre, e.latitud, e.longitud)
        arbol.insertar_edificio(e.nombre, edificio)

    caminos = CaminoDB.query.all()
    for c in caminos:
        grafo.agregar_camino(c.origen, c.destino, c.distancia)

    return arbol, grafo
