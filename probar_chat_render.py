import requests

url_chatbot = "https://incaa-chatbot-demo.onrender.com/chat"
mensaje = {"mensaje": "¿Qué documentación necesito?"}

response = requests.post(url_chatbot, json=mensaje)
print(response.json())
