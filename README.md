# Chatbot Almoço

Este é um projeto em Python que utiliza a biblioteca `pyttsx3` para síntese de fala e a biblioteca `speech_recognition` para reconhecimento de fala. Ele ouve a pergunta do usuário sobre o cardápio de almoço de um determinado dia da semana e responde com o cardápio correspondente. O usuário também pode sair da aplicação dizendo "sair" ou "obrigado".

## Funcionalidades

- Ouve a pergunta do usuário sobre o almoço de um dia específico.
- Responde com o cardápio de almoço para o dia solicitado.
- Utiliza síntese de fala para fornecer a resposta.
- Permite ao usuário encerrar a interação dizendo "sair" ou "obrigado".

## Requisitos

- Python 3.6 ou superior
- Bibliotecas:
  - `pyttsx3`
  - `speech_recognition`
  - `pyaudio` (necessário para `speech_recognition`)

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/marcio-guimaraes/chatbot-almoco.git
    cd chatbot-almoco
    ```

2. Crie um ambiente virtual e ative-o:

    ### No Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    ### No Linux/Mac:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Execute o script principal:

    ```bash
    python main.py
    ```

2. O script irá pedir para você perguntar sobre o almoço. Diga algo como "Qual é o almoço de segunda-feira?".
3. O script irá reconhecer sua pergunta e responderá com o cardápio de almoço do dia solicitado.
4. Para encerrar, diga "sair" ou "obrigado".

## Estrutura do Código

- `main.py`: Contém a lógica principal do programa.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.

## Funções Principais

### `obter_almoco(dia)`

Retorna o cardápio de almoço para o dia da semana especificado.

### `ouvir_pergunta()`

Ouve a pergunta do usuário e a retorna como uma string.

## Desenvolvimento Futuro

Em breve, pretendo desenvolver uma interface gráfica para este projeto, tornando-o mais acessível e fácil de usar. Eventualmente, também planejo integrar essa aplicação em um site para facilitar o acesso ao cardápio de almoço de qualquer lugar.

