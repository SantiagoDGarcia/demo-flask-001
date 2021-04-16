"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 5 + 5
    return "<h3>5 + 5 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
	cadena = ""
	compras = ["Pollo", "Pavo", "Papa", "Leche", "Pescado"]

	for x in compras:
		cadena = '%s<li style ="color:red">%s</li>\n' % (cadena,x)
	return '<h1>Listado de compras</h1> <ul style ="color:red">%s</ul>' % cadena

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
