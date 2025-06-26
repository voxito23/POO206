# Importar las librerias necesarias
from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'DBFLASK'
#app.config['MYSQL_PORT'] = 3306
app.secret_key = 'mysecretkey'


mysql = MySQL(app)

#Ruta de inicio
@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_album')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={}, albums=consultaTodo)
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('formulario.html', errores={}, albums=[])
    finally:
        cursor.close()
        
#Ruta de detalle
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_album WHERE id=%s',(id,))
        consultaId= cursor.fetchone()
        return render_template('consulta.html',album=consultaId)
    except Exception as e:
        print('Error al consultar por id: '+e)
        return redirect(url_for('home'))
    finally:
        cursor.close()        

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

    #Ruta para el insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    
    errores={}
    
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()
    
    if not Vtitulo:
        errores['txtTitulo']= 'Nombre del album obligatorio'
    if not Vartista:
        errores['txtArtista']= 'Nombre del artista obligatorio'
    if not Vanio:
        errores['txtAnio']= 'Año es obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio']= 'Ingresa un año válido'
        
    if not errores:
    
    #Intentamos Ejecutar el INSERT
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tb_album (album, artista, anio) VALUES (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
            mysql.connection.commit() 
            flash('Album guardado con exito') 
            return redirect(url_for('home'))
    
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: ' + str(e))
            return redirect(url_for('home'))
    
        finally:
            cursor.close()
            
    return render_template('formulario.html', errores=errores)    

#Ruta try-catch
@app.errorhandler(404)
def pageNotFound(e):
    return 'Cuidado: Error de capa 8 !!!',404
@app.errorhandler(405)
def methosNotAllowed(e):
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

if __name__ == '_main_':
    app.run(port=3000,debug=True)