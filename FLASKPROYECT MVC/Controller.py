from flask import Blueprint, jsonify
from app import mysql
import MySQLdb

internoBP = Blueprint('interno', __name__)

# Ruta de gestión interna

#ruta try catch
@internoBP.errorhandler(404)
def pageNotFound(e):
    return 'Cuidado: Error de capa 8 !!!', 404

@internoBP.errorhandler(405)
def metodonoP(e):
    return 'Revisa el metodo de envio de tu ruta (GET o POST)', 405

# Ruta para probar la conexion a MySQL
@internoBP.route('/DBCheck')
def DB_check():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        return jsonify({'status': 'ok', 'message': 'Conectado con éxito'}), 200
    except MySQLdb.MySQLError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500