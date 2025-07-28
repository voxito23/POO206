from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.albumModel import *

albumsBP= Blueprint('albums',__name__)

#ruta de inicio
@albumsBP.route('/')
def home():
    try:
        albums= getAll()
        return render_template('formulario.html', errores={}, albums=albums)
    except Exception as e:
        print('Error al consultar todo: '+str(e))
        return render_template('formulario.html', errores={}, albums=[])
    

#ruta album detalles
@albumsBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        album = getById(id)
        return render_template('consulta.html',album=album)
    except Exception as e:
        print('Error al consultar por id: '+str(e))
        return redirect(url_for('albums.home'))
#ruta para guardar
@albumsBP.route('/guardarAlbum', methods=['POST'])
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
            insertAlbum(Vtitulo, Vartista, Vanio)
            flash('Álbum guardado con éxito') 
            return redirect(url_for('albums.home'))
    
        except Exception as e:
            mysql.connection.rollback()
            flash('Algo falló: ' + str(e))
            return redirect(url_for('albums.home'))
            
    return render_template('formulario.html', errores=errores, albums=getAll())

#ruta para editar(abre el form)
@albumsBP.route('/actualizar/<int:id>')
def actualizar(id):
    try:
        album= getById(id)
        return render_template('formUpdate.html', album=album, errores={})
    except Exception as e:
        print('Error al cargar álbum para actualizar: '+str(e))
        return redirect(url_for('albums.home'))
    
#ruta para ejecutar actualizacion
@albumsBP.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizarAlbum(id):
    errores = {}

    Utitulo = request.form.get('txtTitulo', '').strip()
    Uartista = request.form.get('txtArtista', '').strip()
    Uanio = request.form.get('txtAnio', '').strip()

    if not Utitulo:
        errores['txtTitulo']= 'Nombre del album obligatorio'
    if not Uartista:
        errores['txtArtista']= 'Nombre del artista obligatorio'
    if not Uanio:
        errores['txtAnio']= 'Año es obligatorio'
    elif not Uanio.isdigit() or int(Uanio) < 1800 or int(Uanio) > 2100:
        errores['txtAnio']= 'Ingresa un año válido'

    if errores:
        return render_template('formUpdate.html',album=(id, Utitulo, Uartista, Uanio),errores=errores)

    try:
        updateAlbum(id,Utitulo,Uartista,Uanio)
        flash('Álbum actualizado en BD')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))

    return redirect(url_for('albums.home'))

#ruta confirmar delete
@albumsBP.route('/eliminar/<int:id>')
def eliminar(id):
    try:
        album= getById(id)
        return render_template('confirmDel.html', album=album)
    except Exception as e:
          print('Álbum no encontrado: '+str(e))
          return redirect(url_for('albums.home'))
      
#ruta ejecutar delete
@albumsBP.route('/confirmarEliminar/<int:id>', methods=['POST'])
def confirmarEliminar(id):
    try:
        softDeleteAlbum(id)
        flash('Álbum eliminado en BD')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))
    return redirect(url_for('albums.home'))