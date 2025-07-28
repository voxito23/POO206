#crea una app web donde los usuarios pueden registrar restaurantes y deja reseñas
#.,consultar,editar y eliminar sus reseñas una base de datos. de las cuales se guardara;
#restarurante,tipo de comida,comentario,califiacion.
# Importar las librerias necesarias
from flask import Flask,jsonify,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'RESTAURANTE'
#app.config['MYSQL_PORT'] = 3306
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

#Ruta de inicio
@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_comida')
        consultaTodo= cursor.fetchall()
        return render_template('index.html', errores={}, Restaurant=consultaTodo)
    except Exception as e:
        print('Error al consultar todo: '+e)
        return render_template('index.html', errores={}, Restaurant=[])
    finally:
        cursor.close()
        
#Ruta de detalle
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_comida WHERE id=%s',(id,))
        consultaId= cursor.fetchone()
        return render_template('consult.html',Restaurant=consultaId)
    except Exception as e:
        print('Error al consultar por id: '+e)
        return redirect(url_for('home'))
    finally:
        cursor.close()        

#Ruta de ediciom
@app.route('/editar/<int:id>')
def editar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_restaurante WHERE id=%s', (id,))
        restaurante = cursor.fetchone()
        return render_template('actualiz.html', Restaurant=restaurante, errores={})
    except Exception as e:
        print('Error al cargar Reseña para editar: '+str(e))
        flash('No se pudo cargar la reseña')
        return redirect(url_for('home'))
    finally:
        cursor.close()
#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consult.html')

    #Ruta para el insert
@app.route('/guardarreseña', methods=['POST'])
def guardar():
    
    errores={}
    
    Vtitulo = request.form.get('txtRestaurante', '').strip()
    Vartista = request.form.get('txtTipo_de_Comida', '').strip()
    Vanio = request.form.get('txtCalificacion', '').strip()
    
    if not Vtitulo:
        errores['txtRestaurante']= 'Nombre del restaurante obligatorio'
    if not Vartista:
        errores['txtTipo_de_Comida']= 'Nombre del tipo de comida obligatorio'
    if not Vanio:
        errores['txtCalificacion']= 'Calificacion'
    elif not Vanio.isdigit() or int(Vanio) < 0 or int(Vanio) > 5:
        errores['txtCalificacion']= 'Ingresa una calificacion válida'
        
    if not errores:
    
    #Intentamos Ejecutar el INSERT
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tb_restaurante (restaurante, tipo_comida, calificacion) VALUES (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
            mysql.connection.commit() 
            flash('Reseña guardada') 
            return redirect(url_for('home'))
    
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo fallo: ' + str(e))
            return redirect(url_for('home'))
    
        finally:
            cursor.close()
            
    return render_template('index.html', errores=errores) 

#Ruta para actualizar
@app.route('/actualizarRestaurante', methods=['POST'])
def actualizar_album():
    errores = {}
    Vid      = request.form.get('id')
    VRestaurante  = request.form.get('txtRestaurante', '').strip()
    VComida = request.form.get('txtTipo_de_Comida', '').strip()
    Vcalificacion    = request.form.get('txtCalificacion', '').strip()

    if not VRestaurante:
        errores['txtRestaurante']  = 'Nombre del restaurante obligatorio'
    if not VComida:
        errores['txtTipo_de_Comida'] = 'Nombre del tipo de comida obligatorio'
    if not Vcalificacion.isdigit() or int(Vcalificacion) < 0 or int(Vcalificacion) > 5:
        errores['txtCalificacion']    = 'Ingresa una calificacion válida'

    if errores:
     return render_template('actualiz.html',
        album=(Vid, VRestaurante, VComida, Vcalificacion),
        errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            'UPDATE tb_restaurante SET restaurante=%s, tipo_comida=%s, calificacion=%s WHERE id=%s',
            (VRestaurante, VComida, Vcalificacion, Vid)
        )
        mysql.connection.commit()
        flash('Reseña guardada')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo fallo: ' + str(e))
    finally:
        cursor.close()

    return redirect(url_for('home'))
   
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