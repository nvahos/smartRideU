from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmartRide U</title>
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
            select, p {
                font-size: 1.2rem;
                margin: 0.5rem 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>SmartRide U</h1>
            <p>Planifica tus viajes y evita la congestión en el campus</p>
        </header>
        <main>
            <section>
                <h2>Ubicación en tiempo real de los buses</h2>
                <p>Por ahora, esta funcionalidad estará simulada.</p>
                <img src="https://via.placeholder.com/500x300.png?text=Mapa+de+Buses" alt="Mapa de buses">
            </section>
            <section>
                <h2>Recomendaciones para usuarios en carro</h2>
                <p>Selecciona tu zona de residencia para obtener recomendaciones:</p>
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
                        recommendation.textContent = 'Recomendación: Usa la Puerta 4 para entrar al campus.';
                        break;
                    case 'puerto':
                        recommendation.textContent = 'Recomendación: Usa la Puerta 118 para entrar al campus.';
                        break;
                    case 'riomar':
                        recommendation.textContent = 'Recomendación: Usa la Puerta 7 para entrar al campus.';
                        break;
                    default:
                        recommendation.textContent = '';
                }
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
