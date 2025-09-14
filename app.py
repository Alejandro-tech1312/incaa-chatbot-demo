import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Cargar respuestas desde JSON
with open("respuestas_incaa.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    respuestas = data["respuestas"]

# Definir palabras clave para cada pregunta
palabras_clave = [
    {
        "keywords": ["documentación", "inscribirme", "registro"],
        "respuesta": "Generalmente se solicita: formulario de inscripción, DNI o CUIT, guion o tratamiento, presupuesto, equipo técnico y artístico."
    },
    {
        "keywords": ["proyecto independiente", "incorporar proyecto"],
        "respuesta": "Debes enviar un correo electrónico a enlinea@incaa.gob.ar con el asunto 'Incorporación de proyecto independiente'."
    },
    {
        "keywords": ["quién registrarse", "registro público audiovisual", "inscribirse"],
        "respuesta": "Toda persona física o jurídica que ejerza alguna actividad audiovisual en Argentina debe inscribirse en el Registro Público de la Actividad Cinematográfica y Audiovisual."
    },
    {
        "keywords": ["postulo", "comité", "jurado"],
        "respuesta": "Los interesados deben inscribirse a través de la plataforma INCAA en Línea, presentando declaraciones juradas y documentación que acredite su experiencia y trayectoria."
    },
    {
        "keywords": ["exhibir", "festivales", "ciclos"],
        "respuesta": "Se debe solicitar autorización al INCAA a través de la plataforma de trámites a distancia (TAD), efectuado por los responsables de la organización del evento."
    },
    {
        "keywords": ["registro público audiovisual", "inscribirme", "documentación"],
        "respuesta": "Debes completar el formulario de inscripción, presentar DNI o CUIT, constituir un domicilio electrónico y, si corresponde, acompañar la constancia de pago de aranceles."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json.get("mensaje", "").lower()

    for item in palabras_clave:
        # Si alguna de las palabras clave aparece en el mensaje
        if any(keyword.lower() in mensaje for keyword in item["keywords"]):
            return jsonify({"respuesta": item["respuesta"]})

    return jsonify({"respuesta": "No encontré una respuesta para esa pregunta."})

if __name__ == "__main__":
    import os
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
