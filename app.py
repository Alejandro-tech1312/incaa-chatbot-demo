from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "")
    # Tu lógica de respuesta
    respuesta = "Generalmente se solicita: formulario de inscripción, DNI o CUIT, guion o tratamiento, presupuesto, equipo técnico y artístico."
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    import os
    puerto = int(os.environ.get("PORT", 5000))  # Render asigna el puerto vía variable de entorno
    app.run(host="0.0.0.0", port=puerto)

