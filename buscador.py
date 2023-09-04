import requests as re
import json

# Solicita o número do CEP ao usuário
cep = input("Digite o CEP: ")

# Remove o hífen, caso o usuário tenha inserido
cep = cep.replace("-", "")

# Testa se o CEP tem exatamente 8 números
if len(cep) < 8 or len(cep) > 8:
    print("Erro: o CEP deve ter exatamente 8 números")
else:
    # Faz a consulta do CEP via API e retorna no formato JSON em uma váriável
    busca_cep = re.get(f"https://viacep.com.br/ws/{cep}/json/").json()

    # Separamos os dados que queremos em variáveis separadas
    rua = busca_cep['logradouro']
    bairro = busca_cep['bairro']
    cidade = busca_cep['localidade']
    estado = busca_cep['uf']

    # Imprime os dados que queremos separados
    print("Rua: " + rua)
    print("Bairro: " + bairro)
    print("Cidade: " + cidade)
    print("Estado: " + estado)
