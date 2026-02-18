from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

WEATHER_API_KEY = '8b701e1f69a379ae95bb30fbc5060df6'

@app.route('/')
def index():
    return render_template('clima.html')

@app.route('/api/clima')
def obtener_clima():
    try:
        # Si el cliente envía lat/lon, úsalos (mejor precisión). Si no, usar IP.
        lat_param = request.args.get('lat')
        lon_param = request.args.get('lon')
        if lat_param and lon_param:
            try:
                lat = float(lat_param)
                lon = float(lon_param)
            except ValueError:
                return jsonify({'error': 'Coordenadas inválidas'}), 400
            ciudad = request.args.get('ciudad')
        else:
            # Opción 1: ip-api.com (sin API key, más generosa)
            ip_response = requests.get('http://ip-api.com/json/', timeout=5)
            ip_response.raise_for_status()
            ubicacion = ip_response.json()
            
            if ubicacion.get('status') == 'fail':
                return jsonify({'error': 'No se pudo obtener ubicación'}), 400
            
            ciudad = ubicacion.get('city', 'Ciudad desconocida')
            # si no vinieron lat/lon por parámetro, tomarlas de la IP
            if not (lat_param and lon_param):
                lat = ubicacion.get('lat')
                lon = ubicacion.get('lon')
        
        if not lat or not lon:
            return jsonify({'error': 'Coordenadas no disponibles'}), 400
        
        # Obtener clima
        weather_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': lon,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'es'
        }
        
        clima_response = requests.get(weather_url, params=params, timeout=5)
        clima_response.raise_for_status()
        clima = clima_response.json()
        
        if 'main' not in clima or 'weather' not in clima:
            return jsonify({'error': 'Respuesta del clima inválida'}), 400
        
        # Determinar país: preferir datos de `ubicacion` si existen, sino usar respuesta del clima
        if 'ubicacion' in locals() and isinstance(ubicacion, dict):
            pais = ubicacion.get('country', 'Desconocido')
        else:
            pais = clima.get('sys', {}).get('country', 'Desconocido')

        # Determinar nombre de ciudad: preferir el parámetro enviado, sino usar el nombre devuelto por el API de clima
        if ciudad and ciudad.strip():
            ciudad_nombre = ciudad
        else:
            ciudad_nombre = clima.get('name') or (ubicacion.get('city') if 'ubicacion' in locals() else 'Ubicación actual')

        resultado = {
            'ciudad': ciudad_nombre,
            'pais': pais,
            'temperatura': round(clima['main']['temp'], 1),
            'descripcion': clima['weather'][0]['description'].capitalize(),
            'humedad': clima['main']['humidity'],
            'viento': clima['wind']['speed'],
            'icono': clima['weather'][0]['icon']
        }
        
        return jsonify(resultado)
        
    except requests.Timeout:
        return jsonify({'error': 'Tiempo de espera agotado'}), 504
    except requests.RequestException as e:
        return jsonify({'error': f'Error de red: {str(e)}'}), 503
    except (KeyError, IndexError) as e:
        return jsonify({'error': f'Datos incompletos: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)