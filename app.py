from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Base de conocimiento simple
respuestas = {
    "convocatorias": "Podés consultar las convocatorias vigentes en: https://incaa.gob.ar/convocatorias",
    "documentación": "Generalmente se solicita: formulario de inscripción, DNI o CUIT, guion o tratamiento, presupuesto, equipo técnico y artístico.",
    "plazos": "Los plazos de inscripción dependen de cada convocatoria, revisá la sección específica en INCAA en Línea.",
    "contacto": "Podés escribir a atencionalpublico@incaa.gob.ar o llamar al 0800 del INCAA."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("mensaje", "").lower()
    respuesta = "No tengo esa información, te recomiendo revisar la web de INCAA en Línea."
    for clave, valor in respuestas.items():
        if clave in user_input:
            respuesta = valor
            break
    return jsonify({"respuesta": respuesta})

# Heroku asigna el puerto automáticamente
port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
