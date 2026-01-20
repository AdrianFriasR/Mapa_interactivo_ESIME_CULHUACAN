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

    def buscar_materia(self, nombre_materia):
        resultado = []

        horarios = self.horarios.cabeza
        if horarios is not None:
            actual_horario = horarios
            while True:
                if actual_horario.dato.materia.lower() == nombre_materia.lower():
                    resultado.append((self.numero, actual_horario.dato))

                    actual_horario = actual_horario.siguiente
                    if actual_horario == horarios:
                        break

            actual_salon = actual_salon.sig
        return resultado
