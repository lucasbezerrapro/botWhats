from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.generativeai import *
from config.gemini import generate_gemini_content

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return 'bot funcionando'
@app.route('/bot', methods=['POST'])
def bot():
    # Acessa o corpo da mensagem
    mensagem = request.values.get('Body', '').lower()
    
    # Inicializa a resposta do Twilio
    resp = MessagingResponse()
    
    # Definindo msg fora do bloco condicional
    msg = resp.message()

    # Verifica se a mensagem contém a palavra "consulta"
    if 'consulta' in mensagem:
        # Se sim, pergunta se o usuário quer marcar uma consulta
        msg.body('Você gostaria de marcar uma consulta? Responda com "sim" ou "não".')
    elif mensagem == 'sim':
        # Se a resposta for "sim", confirma a marcação da consulta
        msg.body('Consulta marcada.')
    elif mensagem == 'não':
        # Se a resposta for "não", informa ao usuário que não há consulta marcada
        msg.body('Ok, sem problemas. Se precisar de algo mais, estou à disposição.')
    else:
        responseIA = generate_gemini_content(mensagem)
        msg.body(responseIA)
    
    # Retorna a resposta do Twilio
    return str(resp)

if __name__ == '__main__':
    app.run()
