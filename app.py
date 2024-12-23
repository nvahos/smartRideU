from flask import Flask, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    # Información simulada de los buses
    buses = [
        {
            "id": 1,
            "ruta": "Riomar -> Universidad del Norte",
            "ubicacion": [11.0199, -74.8505],
            "puestos": 5,
            "hora": "6:30 AM",
            "tiempo_restante": 10,  # minutos estimados
        },
        {
            "id": 2,
            "ruta": "Norte-Centro Histórico -> Universidad del Norte",
            "ubicacion": [10.997395, -74.828013],
            "puestos": 2,
            "hora": "6:45 AM",
            "tiempo_restante": 20,  # minutos estimados
        },
        {
            "id": 3,
            "ruta": "Suroccidente -> Universidad del Norte",
            "ubicacion": [10.964931, -74.834326],
            "puestos": 10,
            "hora": "7:00 AM",
            "tiempo_restante": 30,  # minutos estimados
        },
    ]

    # HTML con Leaflet.js y cálculo de tiempo
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmartRide U - Universidad del Norte</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f8f9fa;
                color: #333;
            }
            header {
                background: #007bff;
                color: white;
                text-align: center;
                padding: 1.5rem;
            }
            main {
                padding: 1rem;
            }
            section {
                margin-bottom: 2rem;
                background: white;
                padding: 1rem;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            #map {
                width: 100%;
                height: 500px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .info {
                margin: 1rem 0;
                font-size: 1.2rem;
            }
            select {
                padding: 0.5rem;
                font-size: 1rem;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>SmartRide U</h1>
            <p>Buses oficiales hacia y desde la Universidad del Norte</p>
        </header>
        <main>
            <section>
                <h2>Ubicación en tiempo real de los buses</h2>
                <p>Radares en tiempo real muestran la ubicación de los buses:</p>
                <div id="map"></div>
            </section>
            <section>
                <h2>Puerta de ingreso según tu zona de residencia</h2>
                <p>Selecciona tu zona de residencia para conocer la puerta más cercana:</p>
                <select id="zone-selector" onchange="updateRecommendation()">
                    <option value="">Selecciona tu zona</option>
                    <option value="riomar">Riomar</option>
                    <option value="norte-centro">Norte-Centro Histórico</option>
                    <option value="puerto">Puerto Colombia</option>
                    <option value="suroccidente">Suroccidente</option>
                    <option value="suroriente">Suroriente</option>
                    <option value="area-metropolitana">Área Metropolitana</option>
                    <option value="otros-municipios">Otros Municipios</option>
                </select>
                <p id="recommendation" class="info"></p>
            </section>
        </main>
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <script>
            // Inicializar el mapa
            const map = L.map('map').setView([11.0204, -74.8506], 13);

            // Agregar el mapa base de OpenStreetMap
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            // Agregar marcadores para los buses
            const buses = {{ buses|tojson }};
            buses.forEach(bus => {
                const marker = L.marker(bus.ubicacion).addTo(map);
                marker.bindPopup(`
                    <b>Ruta:</b> ${bus.ruta}<br>
                    <b>Puestos disponibles:</b> ${bus.puestos}<br>
                    <b>Hora de salida:</b> ${bus.hora}<br>
                    <b>Tiempo restante:</b> ${bus.tiempo_restante} minutos
                `);
            });

            // Actualizar recomendación de puerta
            function updateRecommendation() {
                const zone = document.getElementById('zone-selector').value;
                const recommendation = document.getElementById('recommendation');

                switch(zone) {
                    case 'riomar':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 7.';
                        break;
                    case 'norte-centro':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4.';
                        break;
                    case 'puerto':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 11.';
                        break;
                    case 'suroccidente':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4.';
                        break;
                    case 'suroriente':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4 o 11.';
                        break;
                    case 'area-metropolitana':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4.';
                        break;
                    case 'otros-municipios':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4 o 7.';
                        break;
                    default:
                        recommendation.textContent = '';
                }
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html, buses=buses)

if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

