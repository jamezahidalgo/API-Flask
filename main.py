from flask import Flask

from routes import Usuario, Tarea

app = Flask(__name__)

@app.route('/')
def index():
    return 'API tareas!'

# Registra los blueprint
app.register_blueprint(Usuario.main, url_prefix="/api/usuarios")
# Para las tareas
app.register_blueprint(Tarea.main, url_prefix="/api/tareas")

app.run(host='0.0.0.0', port=81)
