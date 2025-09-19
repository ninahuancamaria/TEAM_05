from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

# Ruta para el sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'manu.xml', mimetype='application/xml')

# Página principal
@app.route('/')
def home():
    # Llamamos cada imagen por separado
    imagenes = {
        "imagen1": url_for('static', filename='image/ramo1.jpg'),
        "imagen2": url_for('static', filename='image/ramo2.jpg'),
        "imagen3": url_for('static', filename='image/ramo3.png'),
        "imagen4": url_for('static', filename='image/ramo4.png'),
        "imagen5": url_for('static', filename='image/ramo5.jpg'),
        "imagen6": url_for('static', filename='image/ramo6.png'),
        "carrito": url_for('static', filename='image/carrito.png'),
        "favorito": url_for('static', filename='image/favorito.png'),
        "retos": url_for('static', filename='image/retos.gif'),
        "claro/oscuro": url_for('static', filename='image/claro.png'),
        "favorito_rojo": url_for('static', filename='image/favorito-rojo.png'),
        "perfil": url_for('static', filename='image/perfil.png'),
        "descuento1": url_for('static', filename='image/descuento1.png'),
        "descuento2": url_for('static', filename='image/descuento2.png'),
        "descuento3": url_for('static', filename='image/descuento3.png'),
        "descuento4": url_for('static', filename='image/descuento4.png'),
        "descuento5": url_for('static', filename='image/descuento5.png'),
        "descuento6": url_for('static', filename='image/descuento6.png'),
        "descuento7": url_for('static', filename='image/descuento7.png'),
        "buscador": url_for('static', filename='image/buscador.png')
    }

    return render_template('index.html', **imagenes)

# Página de formulario
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
