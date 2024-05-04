from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from config.gemini import generate_content
import os
import google.generativeai as genai

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Funcionou'

@app.route('/bot', methods=['POST'])
def bot():
    # Imprime os valores recebidos na solicitação POST
    print(request.values)

    # Acessa o corpo da mensagem
    mensagem = request.values.get('Body', '')

    # Chama a função gemini() e armazena a resposta
    resposta_gemini = generate_content(mensagem)

    # Cria uma resposta do Twilio
    resp = MessagingResponse()
    msg = resp.message()

    # Define a resposta do bot como a resposta do Gemini
    msg.body(resposta_gemini)

    # Retorna a resposta como uma string
    return str(resp)

if __name__ == '__main__':
    app.run()
