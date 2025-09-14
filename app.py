from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Cargar respuestas desde el archivo JSON
with open("respuestas_incaa.json", "r", encoding="utf-8") as f:
    respuestas = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pregunta = data.get("mensaje", "").lower()

    # Buscar respuesta
    respuesta = respuestas.get(pregunta, "Lo siento, no tengo información para esa consulta.")
    
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    # Para Render: host 0.0.0.0 y puerto dinámico
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
