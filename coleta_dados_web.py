import requests
from bs4 import BeautifulSoup

url = 'https://bindingofisaacrebirth.fandom.com/wiki/Binding_of_Isaac:_Rebirth_Wiki'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Exibir o texto
#print(extracao.text.strip())

#Filtrar a exibição pela tag
cont_titulo = 0
cont_paragrafo = 0

# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name == 'h2':
#         cont_titulo += 1
#     elif linha_texto.name == 'p':
#         cont_paragrafo += 1
#
#
# print('Total de titulos:', cont_titulo)
# print('Total de paragrafos: ', cont_paragrafo)


# for linha_texto in extracao.find_all(['h2','p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print ('Titulo: \n', titulo)
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo: \n', paragrafo)

for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link: ', a.text.strip(), ' | URL:', a["href"])