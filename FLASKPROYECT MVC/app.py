from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb
from config import Config

app= Flask(__name__)

mysql = MySQL()

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumcontroller import albumsBP
    app.register_blueprint(albumsBP)
    
    return app

#RUTAS DE GESTION INTERNA

#Ruta try-catch
@app.errorhandler(404)
def pageNotFound(e):
    return 'Cuidado: Error de capa 8 !!!',404
@app.errorhandler(405)
def methodNotAllowed(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)',405

#Ruta para probar la conexion a MySQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify( {'status':'ok','message':'Conectado con exito'} ),200
    except MySQLdb.MySQLError as e:
        return jsonify( {'status':'error','message':str(e)} ),500

if __name__ == '__main__':
    app = create_app()
    app.run(port=3000,debug=True)