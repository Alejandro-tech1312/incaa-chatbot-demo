from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ruta principal que sirve el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el chatbot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    
    # Aquí tu lógica de respuesta
    respuesta = "Generalmente se solicita: formulario de inscripción, DNI o CUIT, guion o tratamiento, presupuesto, equipo técnico y artístico."
    
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto dinámicamente
    app.run(host='0.0.0.0', port=port)
