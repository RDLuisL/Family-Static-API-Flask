"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# Importaciones System): Módulo para interactuar con el sistema operativo.
# Flask: Clase principal para crear aplicaciones web con Flask.
# request: Objeto para manejar las solicitudes HTTP.
# jsonify: Función para convertir objetos Python a respuestas JSON.
# url_for: Función para construir URLs.
# CORS: Clase para habilitar CORS (Cross-Origin Resource Sharing).
# Protocolos de Seguridad: APIException: Clase para manejar excepciones personalizadas.
# Base de datos: generate_sitemap: Función para generar un sitemap.

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Creamos una instancia de la aplicación Flask.
# app.url_map.strict_slashes = False: Configuración para permitir rutas con o sin barra inclinada 
# al final.
# CORS(app): Habilita CORS en la aplicación para permitir solicitudes desde diferentes dominios.

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)
# Se define una ruta / que devuelve un sitemap generado a partir de los endpoints de la aplicación.

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200


    

@app.route('/member/<int:member_id>', methods=['GET'])
# /members (GET): Devuelve información sobre todos los miembros de la familia Jackson.
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    return jsonify(member), 200
# /member/<int:member_id> (GET): Devuelve información sobre un miembro específico de la familia
#  Jackson.

@app.route('/member', methods=['POST'])
def add_member():
    body_last_name = request.json.get("last_name")
    body_name = request.json.get("first_name")
    body_age = request.json.get("age")
    body_id = request.json.get("id")
    body_lucky_numbers = request.json.get("lucky_numbers")
    member = {
        "id": body_id or jackson_family._generateId(),
        "first_name": body_name,
        "last_name": body_last_name,
        "age": body_age,
        "lucky_numbers": body_lucky_numbers,
    }
    jackson_family.add_member(member)
    return jsonify(None), 200
# /member (POST): Agrega un nuevo miembro a la familia Jackson con la información proporcionada en el cuerpo de la solicitud JSON.


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_one_member(member_id):
    member = jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200
# /member/<int:member_id> (DELETE): Elimina un miembro específico de la familia Jackson.

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
# Ejecución de la aplicación:
# El bloque if __name__ == '__main__': asegura que el servidor se inicie solo si se ejecuta el 
# script directamente.
# El número de puerto se obtiene de la variable de entorno PORT o se utiliza el valor predeterminado
#  3000.
# La aplicación se ejecuta en el host '0.0.0.0', haciendo que sea accesible desde cualquier dirección IP en la red, 
# y se habilita el modo de depuración (debug=True).