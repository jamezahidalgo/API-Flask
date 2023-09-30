from flask import Blueprint, jsonify, request
# Model
from models.UsuarioModel import UsuarioModel
# Entities
from models.entities.Usuario import Usuario

main = Blueprint("usuario_blueprint", __name__)

@main.route("/")
def getUsuarios():
  try:    
    usuarios = UsuarioModel.getUsuarios()
    return jsonify(usuarios)
  except Exception as ex:
    return jsonify({"msg" : str(ex)}), 500  

@main.route("/add", methods = ['POST'])
def add_usuario():
  try:
    nuevo = Usuario(request.json['email'], request.json['nombre'])
    if UsuarioModel.add_user(nuevo):
      return jsonify(nuevo.email)
    else:
      return jsonify({"message" : "Error al insertar"}), 500    
  except Exception as ex:
    return jsonify({"message" : str(ex)}), 500  