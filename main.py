import pyttsx3
import speech_recognition as sr
import re

def obter_almoco(dia):
    if dia == "segunda":
        return "O almoço de segunda-feira será salada, carne moída com batata, arroz branco, feijão carioca, macarrão parafuso e fruta."
    elif dia == "terça":
        return "O almoço de terça-feira será salada, arroz com frango, feijão carioca, purê de batata doce e fruta."
    elif dia == "quarta":
        return "O almoço de quarta-feira será vinagrete, iscas de frango acebolado, arroz branco, feijão carioca, farofa e fruta."
    elif dia == "quinta":
        return "O almoço de quinta-feira será Frango ao molho com abóbora, salada de repolho, alface e pepino, arroz branco, feijão carioca e uma fruta de sobremesa."
    elif dia == "sexta":
        return "O almoço de sexta-feira será Estrogonofe de carne, salada de alface, rúcula e tomate, arroz branco, feijão carioca, Batata palha e uma fruta de sobremesa."
    elif dia == "sábado" or dia == "sabado":
        return "Não há almoço para sábado"
    else:
        return "Desculpe, não tenho informações sobre o almoço desse dia."

def ouvir_pergunta():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga o que você deseja saber sobre o almoço (ou 'sair' para encerrar): ")
        audio = recognizer.listen(source)

    try:
        pergunta = recognizer.recognize_google(audio, language="pt-BR")
        print("Pergunta: ", pergunta)
        return pergunta.lower()
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o áudio.")
        return ""
    except sr.RequestError:
        print("Desculpe, ocorreu um erro durante o reconhecimento de fala.")
        return ""

engine = pyttsx3.init()

while True:
    pergunta = ouvir_pergunta()

    if pergunta == "sair" or pergunta == "obrigado":
        print("Tenha um bom dia!")
        engine.say("Obrigado pela sua interação")
        engine.runAndWait()
        break

    match = re.search(r"(segunda|terça|quarta|quinta|sexta|sábado|sabado)", pergunta)
    if match:
        dia = match.group(0)
        resposta = obter_almoco(dia)
    else:
        resposta = "Desculpe, não entendi a pergunta. Por favor, tente novamente."

    engine.say(resposta)
    engine.runAndWait()
