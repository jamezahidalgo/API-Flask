class Usuario():
  def __init__(self, email = None, nombre = None):
    self.email = email
    self.nombre = nombre
  
  def to_JSON(self):
    return {
      "email" : self.email,
      "nombre" : self.nombre
    }