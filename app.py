from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Información simulada de los buses
    buses = [
        {"id": 1, "ruta": "Centro a Norte", "ubicacion": "Puerta 4", "hora": "6:45 AM"},
        {"id": 2, "ruta": "Puerto Colombia a Riomar", "ubicacion": "Puerta 11", "hora": "7:15 AM"},
        {"id": 3, "ruta": "Riomar a Centro", "ubicacion": "Puerta 7", "hora": "7:45 AM"},
    ]

    # HTML de la aplicación con la nueva funcionalidad
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmartRide U - Universidad del Norte</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f4f4f9;
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
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid #ddd;
                padding: 0.5rem;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            select, p {
                font-size: 1.2rem;
                margin: 0.5rem 0;
            }
            .map-container {
                text-align: center;
                margin: 1rem 0;
            }
            .map-container img {
                max-width: 100%;
                border: 2px solid #ddd;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>SmartRide U</h1>
            <p>Buses oficiales de la Universidad del Norte</p>
        </header>
        <main>
            <section>
                <h2>Ubicación en tiempo real de los buses</h2>
                <p>Radares informan la ubicación de los buses en tiempo real:</p>
                <div class="map-container">
                    <img src="https://via.placeholder.com/800x400.png?text=Mapa+con+Ubicaci%C3%B3n+de+Buses" alt="Mapa de ubicación de buses">
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Ruta</th>
                            <th>Ubicación Actual</th>
                            <th>Hora</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for bus in buses %}
                        <tr>
                            <td>{{ bus.id }}</td>
                            <td>{{ bus.ruta }}</td>
                            <td>{{ bus.ubicacion }}</td>
                            <td>{{ bus.hora }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </section>
            <section>
                <h2>Puerta de ingreso según tu zona de residencia</h2>
                <p>Selecciona tu zona de residencia para conocer la puerta más cercana:</p>
                <select id="zone-selector" onchange="updateRecommendation()">
                    <option value="">Selecciona tu zona</option>
                    <option value="norte-centro">Norte-Centro Histórico</option>
                    <option value="puerto">Puerto Colombia</option>
                    <option value="riomar">Riomar</option>
                </select>
                <p id="recommendation"></p>
            </section>
        </main>
        <script>
            function updateRecommendation() {
                const zone = document.getElementById('zone-selector').value;
                const recommendation = document.getElementById('recommendation');

                switch(zone) {
                    case 'norte-centro':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 4.';
                        break;
                    case 'puerto':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 11.';
                        break;
                    case 'riomar':
                        recommendation.textContent = 'Puerta de ingreso: Puerta 7.';
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

