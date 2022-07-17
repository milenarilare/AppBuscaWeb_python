import requests
from tqdm import tqdm


def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
     with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)

if __name__ == '__main__':
    baixar_arquivo('https://esaj.tjsp.jus.br/petpg/api/protocolos/8W000001E9N3/recibo?instancia=PG','recibo.pdf')
