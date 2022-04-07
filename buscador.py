import requests
import json

def localiza_cep(numero_cep):
    cep_usuario = numero_cep
    api = 'https://cep.awesomeapi.com.br/:json/:'
    link = api + cep_usuario
    resposta = requests.get(link)
    endereco_dic = resposta.json()

    for k, v in endereco_dic.items():
        if k == 'status':
            if v == 400:
               print('CEP invalido')
            elif v == 404:
                print('Cep não encontrado')
        elif k == 'cep':
            print(f'{endereco_dic["address"]}-{endereco_dic["city"]}/{endereco_dic["state"]}')
