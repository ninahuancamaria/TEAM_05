from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Llamamos cada imagen por separado
    imagen1 = url_for('static', filename='image/ramo1.png')
    imagen2 = url_for('static', filename='image/ramo2.png')
    imagen3 = url_for('static', filename='image/ramo3.png')
    imagen4 = url_for('static', filename='image/ramo4.png')
    carrito = url_for('static', filename='image/carrito.png')
    favorito = url_for('static', filename='image/favorito.png')
    perfil = url_for('static', filename='image/perfil.png')
    descuento1 = url_for('static', filename='image/descuento1.png')
    descuento2 = url_for('static', filename='image/descuento2.png')
    descuento3 = url_for('static', filename='image/descuento3.png')
    descuento4 = url_for('static', filename='image/descuento4.png')
    descuento5 = url_for('static', filename='image/descuento5.png')
    buscador = url_for('static', filename='image/buscador.png')


    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
