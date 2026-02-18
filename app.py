# Importaciones
from flask import Flask, render_template, jsonify
import requests

# Crear instancia de Flask
app = Flask(__name__)

# Configuración para desarrollo
app.config['DEBUG'] = True

# Constante de la API
API_URL = "https://jsonplaceholder.typicode.com/users"


def obtener_usuarios():
    """
    Consume la API JSONPlaceholder
    Returns:
        dict: {
            exito (bool),
            datos (list),
            error (str | None)
        }
    """
    try:
        respuesta = requests.get(API_URL, timeout=5)
        respuesta.raise_for_status()

        # ❌ antes: respuesta.json
        # ✅ correcto:
        usuarios = respuesta.json()

        return {
            'exito': True,
            'datos': usuarios,
            'error': None
        }

    except requests.exceptions.Timeout:
        return {
            'exito': False,
            'datos': [],
            'error': 'El API tardó demasiado en responder. Intente nuevamente.'
        }

    except requests.exceptions.HTTPError as e:
        return {
            'exito': False,
            'datos': [],
            'error': f'Error HTTP: {e}'
        }

    except Exception as e:
        return {
            'exito': False,
            'datos': [],
            'error': f'Error inesperado: {str(e)}'
        }


def procesar_datos_usuarios(usuarios):
    """
    Simplifica los datos devueltos por la API
    """
    usuarios_procesados = []

    for usuario in usuarios:
        usuario_simple = {
            'id': usuario.get('id'),
            'nombre': usuario.get('name'),
            'usuario': usuario.get('username'),
            'email': usuario.get('email'),
            'telefono': usuario.get('phone'),
            'ciudad': usuario.get('address', {}).get('city', 'N/A'),
            'empresa': usuario.get('company', {}).get('name', 'N/A')
        }
        usuarios_procesados.append(usuario_simple)

    return usuarios_procesados


# -------------------- RUTAS --------------------

@app.route('/')
def index():
    """
    Ruta principal
    """
    return render_template('index.html')


@app.route('/consultar-usuarios')
def consultar_usuarios():
    """
    Endpoint que consulta usuarios y devuelve JSON al frontend
    """
    resultado = obtener_usuarios()

    if resultado['exito']:
        usuarios_procesados = procesar_datos_usuarios(resultado['datos'])

        return jsonify({
            'exito': True,
            'total': len(usuarios_procesados),
            'usuarios': usuarios_procesados
        })
    else:
        return jsonify({
            'exito': False,
            'error': resultado['error']
        }), 500


# -------------------- MAIN --------------------

if __name__ == '__main__':
    print("=" * 50)
    print("Servidor Flask iniciado")
    print("Accede a: http://localhost:5000")
    print("Presiona CTRL + C para detener el servidor")
    print("=" * 50)

    app.run(host='0.0.0.0', port=5000, debug=True)