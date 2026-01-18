from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class EdificioDB(db.Model):
    __tablename__ = "edificios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), unique=True, nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "lat": self.latitud,
            "lon": self.longitud
        }

class CaminoDB(db.Model):
    __tablename__ = "caminos"

    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(50), nullable=False)
    destino = db.Column(db.String(50), nullable=False)
    distancia = db.Column(db.Float, nullable=False)
