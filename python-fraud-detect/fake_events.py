import numpy as np



def DetectFakeEvent(event_name, event_code):

    #f = open("D:\GIT\jd-python-samples\python-fraud-detect\suspicious_words.txt", "r")

    #lista = [f.read()]

    print('')


def Filter(string, substr): 
    return [str for str in string if
             any(sub in str for sub in substr)] 


#DetectFakeEvent('teste', 4)
event_name = 'Xpower Force funciona Preço boleto farmacia tomar onde comprar XpowerForce?'
list_name = event_name.split()
print(list_name)

fileName = "D:\\Joao\\GIT\\jd-python-samples\\python-fraud-detect\\black_list.txt"
fileList = [line.rstrip('\n') for line in open(fileName, 'r')]
print(fileList)


#print(filter(lambda x: 'Forcecxsd' in x, list_name))

matching = [s for s in fileList if any(xs in s for xs in list_name)]
print(matching)

print(Filter(fileList, list_name))



# ler o arquivo, criar um dicionario com código do evento, quebrar json de pagamento

# depois de pegar o json realizar a busca do campo CPF no JSON (exemplo de filtro)
# beyond_ascii = list(filter(lambda c: c>127, map(ord, symbols)))

# realizar busca na internet do nome do cartão no CPF

# criar banco para mapear compras com mesmo cartão, cpf do cartão, telefone, endereço
