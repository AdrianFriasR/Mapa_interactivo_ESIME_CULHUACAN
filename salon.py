from lista_circular import ListaCircular
from datetime import datetime

class Salon:
    def __init__(self, numero):
        self.numero = numero
        self.horarios = ListaCircular()

    def agregar_horario(self, horario):
        self.horarios.insertar(horario)

    def mostrar_horarios(self):
        self.horarios.recorrer()

    def __str__(self):
        return f"Salon {self.numero}"


    def clase_actual(self):
        if self.horarios.cabeza is None:
            return None

        ahora = datetime.now().strftime("%H:%M")
        actual = self.horarios.cabeza

        while True:
            h = actual.dato
            if h.hora_inicio <= ahora <= h.hora_fin:
                return h

            actual = actual.siguiente
            if actual == self.horarios.cabeza:
                break

        return None
    
    def salon_vacío(self, numero_salon):
        salon = self.buscar_salon(numero_salon)
        if salon is None:
            return True
        return salon.horarios.cabeza is None
    
    def salon_ocupado(self, numero_salon):
        salon = self.buscar_salon(numero_salon)
        if salon is None:
            return False
        return salon.clase_actual() is not None  
    
    def maestro_en_salon(self, numero_salon, nombre_maestro):
        salon = self.buscar_salon(numero_salon)
        if salon is None:
            return False

        actual = salon.horarios.cabeza
        if actual is not None:
            while True:
                if actual.dato.maestro == nombre_maestro:
                    return True

                actual = actual.siguiente
                if actual == salon.horarios.cabeza:
                    break

        return False