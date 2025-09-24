from flask import Flask, render_template, url_for, send_from_directory, send_file

app = Flask(__name__)

# Ruta para el sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'manu.xml', mimetype='application/xml')

# Página principal
@app.route('/')
def home():
    audio = {
        "audioRamo1": url_for('static', filename='audio/alma de bosque.wav'),
        "audioRamo2": url_for('static', filename='audio/aurora moderna.wav'),
        "audioRamo3": url_for('static', filename='audio/atetish.wav'),
        "audioRamo4": url_for('static', filename='audio/belicate.wav'),
        "audioRamo5": url_for('static', filename='audio/canto de rio.wav'),
        "audioRamo6": url_for('static', filename='audio/clicken lila.wav'),
        "audioRamo7": url_for('static', filename='audio/corazón de jardin.wav'),
        "audioRamo8": url_for('static', filename='audio/deliccat.wav'),
        "audioRamo9": url_for('static', filename='audio/dulce amanecer.wav'),
        "audioRamo10": url_for('static', filename='eco de primavera.wav'),
        "audioRamo11": url_for('static', filename='elegancia pura.wav'),
        "audioRamo12": url_for('static', filename='elixir de flores.wav'),
        "audioRamo13": url_for('static', filename='eterno romance.wav'),


    }
    # Llamamos cada imagen por separado
    imagenes = {
        "whatsapp": url_for('static', filename='image/logos/whatsapp.png'),
        "imagen1": url_for('static', filename='image/ramos/ramo1.jpg'),
        "imagen2": url_for('static', filename='image/ramos/ramo2.jpg'),
        "imagen3": url_for('static', filename='image/ramos/ramo3.png'),
        "imagen4": url_for('static', filename='image/ramos/ramo4.png'),
        "imagen5": url_for('static', filename='image/ramos/ramo5.jpg'),
        "imagen6": url_for('static', filename='image/ramos/ramo6.png'),
        "imagen7": url_for('static', filename='image/ramos/ramo7.jpg'),
        "imagen8": url_for('static', filename='image/ramos/ramo8.jpg'),
        "imagen9": url_for('static', filename='image/ramos/ramo9.jpg'),
        "imagen10": url_for('static', filename='image/ramos/ramo10.png'),
        "imagen11": url_for('static', filename='image/ramos/ramo11.jpg'),
        "imagen12": url_for('static', filename='image/ramos/ramo12.jpg'),
        "imagen13": url_for('static', filename='image/ramos/ramo13.png'),
        "carrito": url_for('static', filename='image/logos/carrito.png'),
        "carrito2": url_for('static', filename='image/logos/carrito2.png'),
        "favorito": url_for('static', filename='image/logos/favorito.png'),
        "favorito2": url_for('static', filename='image/logos/favorito2.png'),
        "retos": url_for('static', filename='image/logos/retos.gif'),
        "claro/oscuro": url_for('static', filename='image/logos/claro.png'),
        "oscuro/claro": url_for('static', filename='image/logos/oscuro.png'),
        "favorito_rojo": url_for('static', filename='image/logos/favorito-rojo.png'),
        "perfil": url_for('static', filename='image/logos/perfil.png'),
        "perfil2": url_for('static', filename='image/logos/perfil2.png'),
        "descuento1": url_for('static', filename='image/descuentos/descuento1.png'),
        "descuento2": url_for('static', filename='image/descuentos/descuento2.png'),
        "descuento3": url_for('static', filename='image/descuentos/descuento3.png'),
        "descuento4": url_for('static', filename='image/descuentos/descuento4.png'),
        "descuento5": url_for('static', filename='image/descuentos/descuento5.png'),
        "descuento6": url_for('static', filename='image/descuentos/descuento6.png'),
        "descuento7": url_for('static', filename='image/descuentos/descuento7.png'),
        "buscador": url_for('static', filename='image/logos/buscador.png')
    }

    return render_template('index.html', **imagenes, **audio)


@app.route('/envio')
def envio():
    return render_template('envio.html')
@app.route('/normal')
def normal():
    return render_template('normal.html')

@app.route('/tema-oscuro')
def oscuro():
    return render_template('oscuro.html')


# Página de formulario
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
