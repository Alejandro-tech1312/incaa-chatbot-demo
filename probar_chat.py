import requests

url_chatbot = "http://127.0.0.1:5000/chat"
mensaje = {"mensaje": "¿Qué documentación necesito?"}
response = requests.post(url_chatbot, json=mensaje)
print(response.json())
