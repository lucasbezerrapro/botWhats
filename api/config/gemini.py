import google.generativeai as genai

def generate_gemini_content(prompt):
    # Chave API
    chave = 'AIzaSyDv4Hp2d5GA0WvaWyTvrjR2gNNW83YnS58'

    # Configuração da API
    genai.configure(api_key=chave)

    # Instanciando o modelo
    model = genai.GenerativeModel('gemini-pro')

    # Gerando conteúdo com base no prompt
    response = model.generate_content(prompt)
    
    # Remover asteriscos da resposta
    text = response.text.replace('*', '')

    return text

#while True:
#    msg = input("Você: ")

#    print("BOT: ", generate_gemini_content(msg))
