from graficos import *
from buscador import *

while True:

    grafico('DIGITE SEU CEP')
    usuario = input('CEP: ')
    localiza_cep(usuario)
    linha()
    sair = input('Digite: 1 -Para sair ou  2 - Para continuar:')
    if sair == '1':
        break
    else:
        continue
