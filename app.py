from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Información simulada de los buses
    buses = [
        {"id": 1, "ruta": "Localidad A -> Universidad del Norte", "ubicacion": "Puerta 4", "puestos": 5, "hora": "6:30 AM"},
        {"id": 2, "ruta": "Universidad del Norte -> Localidad B", "ubicacion": "Calle 76", "puestos": 2, "hora": "6:45 AM"},
        {"id": 3, "ruta": "Localidad C -> Universidad del Norte", "ubicacion": "Calle 72", "puestos": 10, "hora": "7:00 AM"},
    ]

    # HTML con las actualizaciones
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
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
            }
            table, th, td {
                border: 1px solid #ddd;
                padding: 0.8rem;
                text-align: center;
            }
            th {
                background-color: #007bff;
                color: white;
            }
            .map-container {
                text-align: center;
                margin: 1rem 0;
            }
            .map-container img {
                max-width: 100%;
                border: 2px solid #ddd;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .info {
                margin: 1rem 0;
                font-size: 1.2rem;
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
                <p>Radares en tiempo real informan sobre la ubicación de los buses y su estado:</p>
                <div class="map-container">
                    <img src="https://via.placeholder.com/800x400.png?text=Simulador+de+Mapa+de+Buses" alt="Mapa de ubicación de los buses">
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Ruta</th>
                            <th>Ubicación Actual</th>
                            <th>Puestos Disponibles</th>
                            <th>Hora de Salida</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for bus in buses %}
                        <tr>
                            <td>{{ bus.id }}</td>
                            <td>{{ bus.ruta }}</td>
                            <td>{{ bus.ubicacion }}</td>
                            <td>{{ bus.puestos }}</td>
                            <td>{{ bus.hora }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </section>
        </main>
    </body>
    </html>
    '''
    return render_template_string(html, buses=buses)

if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

