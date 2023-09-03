import requests as re
import json

# Solicita o número do CEP ao usuário
cep = input("Digite o CEP: ")

# Remove o hífen, caso o usuário tenha inserido
cep = cep.replace("-", "")

# Testa se o CEP tem exatamente 8 números
if len(cep) < 8 and len(cep) > 8:
    print("Erro: o CEP deve ter exatamente 8 números")
else:
    # Faz a consulta do CEP via API e retorna no formato JSON em uma váriável
    busca_cep = re.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    # Separamos os dados que queremos em variáveis separadas
    rua = busca_cep['address_name']
    bairro = busca_cep['district']
    cidade = busca_cep['city']
    estado = busca_cep['state']

    # Imprime os dados que queremos separados
    print("Rua: " + rua)
    print("Bairro: " + bairro)
    print("Cidade: " + cidade)
    print("Estado: " + estado)
