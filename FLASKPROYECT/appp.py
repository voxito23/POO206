from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return 'Hola Mundo FLASK ;)'

#ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola ' + nombre + '!!!'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    