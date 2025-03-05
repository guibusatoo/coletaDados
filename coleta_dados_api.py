import requests
import json

def enviar_arquivo():
    # Definição do caminho do arquivo
    caminho = r"C:\Users\busat\Downloads\produtos_informatica.xlsx"

    # URL do serviço de upload
    url = "https://file.io"

    # Abrir o arquivo e enviá-lo
    with open(r"C:\Users\busat\Downloads\produtos_informatica.xlsx", "rb") as arquivo:
        response = requests.post(url, files={"file": arquivo})

    # Processar a resposta
    for line in response.text.splitlines():
        if "https://file.io/" in line:
            try:
                data = json.loads(line)
                print("JSON data:", data)

                # Exibir informações do arquivo enviado
                print("Link:", data.get("link", "Não disponível"))
                print("Key:", data.get("key", "Não disponível"))

            except json.JSONDecodeError as e:
                print("Erro ao decodificar JSON:", e)
                print("Linha bruta:", line)
            break

def receber_arquivo(file_url):

    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo', requisicao.json)

enviar_arquivo()
receber_arquivo('https://file.io/2ojE41')