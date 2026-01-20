class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, materia, grupo, docente, carrera=None):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.materia = materia
        self.grupo = grupo
        self.docente = docente
        self.carrera = carrera

    def __str__(self):
        return f"{self.dia} {self.hora_inicio}-{self.hora_fin} | {self.materia} ({self.grupo})"
    
    def es_dia_laboral(self):
        dias_laborales = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        return self.dia in dias_laborales
    
    def es_dia_fin_de_semana(self):
        dias_fin_de_semana = ["Sábado", "Domingo"]
        return self.dia in dias_fin_de_semana  
    
    def hoarios_turno_matutino(self):
        return "07:00" <= self.hora_inicio < "13:00"
    
        
    def horarios_turno_vespertino(self):
        return "16:00" <= self.hora_inicio < "22:00"

    
    def es_carrera(self):
        return self.carrera is not None
    
    def clases_por_materia_y_carrera(self, nombre_materia, nombre_carrera):
        return self.materia == nombre_materia and self.carrera == nombre_carrera

    def clases_por_maestro(self, nombre_maestro):
        return self.docente == nombre_maestro
    
    def clases_por_grupo(self, nombre_grupo):
        return self.grupo == nombre_grupo
    

