# Service DB
from database.db import get_connection
# Entities
from models.entities.Usuario import Usuario

class UsuarioModel():
  @classmethod
  def getUsuarios(self):    
    try:
      # Obtener la conexión
      cx = get_connection()
      usuarios = []
      with cx.cursor() as cursor:
        
        cursor.execute("SELECT email, nombre FROM usuario ORDER BY email")
        resultset = cursor.fetchall()
        
        for row in resultset:
          usuario = Usuario(row[0], row[1])
          usuarios.append(usuario.to_JSON())
      cx.close()
      return usuarios
    except Exception as ex:
      return Exception(ex)

  @classmethod
  def add_user(self, user):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute("INSERT INTO usuario VALUES(%s, %s)", (user.email, user.nombre))
        cx.commit()
      cx.close()
      return cursor.rowcount
    except Exception as ex:
      return Exception(ex)