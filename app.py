import json
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Cargar respuestas desde JSON
with open("respuestas_incaa.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    respuestas = data["respuestas"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json.get("pregunta", "").strip().lower()
    respuesta = "No encontré una respuesta para esa pregunta."
    
    for item in respuestas:
        if item["pregunta"].lower() == mensaje:
            respuesta = item["respuesta"]
            break
    
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
