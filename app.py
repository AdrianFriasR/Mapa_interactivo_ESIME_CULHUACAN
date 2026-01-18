from flask import Flask, request, jsonify
from models import db, EdificioDB, CaminoDB
from repositorio import cargar_sistema
from navegacion import calcular_ruta_usuario
from edificio import Edificio

app = Flask(__name__)

# Configuración de la base de datos

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Inicializar sistema (AVL + Grafo)

with app.app_context():
    db.create_all()
    arbol, grafo = cargar_sistema()

# POST /edificios

@app.route("/edificios", methods=["POST"])
def crear_edificio():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "nombre" not in data or "lat" not in data or "lon" not in data:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    try:
        nombre = str(data["nombre"]).strip()
        lat = float(data["lat"])
        lon = float(data["lon"])
    except (ValueError, TypeError):
        return jsonify({"error": "Datos inválidos"}), 400

    # Verificar si ya existe

    existe = EdificioDB.query.filter_by(nombre=nombre).first()
    if existe:
        return jsonify({"error": "El edificio ya existe"}), 409

    # Guardar en base de datos

    edificio_db = EdificioDB(
        nombre=nombre,
        latitud=lat,
        longitud=lon
    )
    db.session.add(edificio_db)
    db.session.commit()

    # Crear objeto de dominio

    edificio = Edificio(nombre, lat, lon)

    # Insertar en AVL

    arbol.insertar_edificio(nombre, edificio)

    return jsonify({
        "mensaje": "Edificio creado correctamente",
        "edificio": edificio_db.to_dict()
    }), 201


@app.route("/caminos", methods=["POST"])
def crear_camino():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    if "origen" not in data or "destino" not in data or "distancia" not in data:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    origen = data["origen"]
    destino = data["destino"]

    try:
        distancia = float(data["distancia"])
    except (ValueError, TypeError):
        return jsonify({"error": "Distancia inválida"}), 400

    # Verificar edificios en BD
    e1 = EdificioDB.query.filter_by(nombre=origen).first()
    e2 = EdificioDB.query.filter_by(nombre=destino).first()

    if not e1 or not e2:
        return jsonify({"error": "Uno o ambos edificios no existen"}), 404

    # Guardar camino en BD
    camino_db = CaminoDB(
        origen=origen,
        destino=destino,
        distancia=distancia
    )
    db.session.add(camino_db)
    db.session.commit()

    # Insertar en grafo (bidireccional)
    grafo.agregar_arista(origen, destino, distancia)

    return jsonify({
        "mensaje": "Camino creado correctamente",
        "camino": camino_db.to_dict()
    }), 201


# POST /ruta

@app.route("/ruta", methods=["POST"])
def obtener_ruta():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    if "lat" not in data or "lon" not in data:
        return jsonify({"error": "Faltan coordenadas"}), 400

    try:
        lat = float(data["lat"])
        lon = float(data["lon"])
    except (ValueError, TypeError):
        return jsonify({"error": "Coordenadas inválidas"}), 400

    resultado = calcular_ruta_usuario(
        lat,
        lon,
        arbol,
        grafo
    )

    return jsonify(resultado), 200

# GET /

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "API de Navegación del Campus activa",
        "endpoints": {
            "POST /edificios": "Registrar edificios",
            "POST /ruta": "Calcular ruta con GPS real"
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
