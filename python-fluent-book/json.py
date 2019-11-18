# Ler arquivos JSON para trabalhar com listas
import json

# ler o arquivo, criar um dicionario com código do evento, quebrar json de pagamento
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

# depois de pegar o json realizar a busca do campo CPF no JSON (exemplo de filtro)
beyond_ascii = list(filter(lambda c: c>127, map(ord, symbols)))

# realizar busca na internet do nome do cartão no CPF

# criar banco para mapear compras com mesmo cartão, cpf do cartão, telefone, endereço
