import requests
import json

api_url = 'https://api.nasa.gov/planetary/apod?api_key=PJxvA17EqASRTmueTK6HeL5hWT7Qm3NgCqGe11JY'
requests = requests.get(api_url)
if requests.status_code == 200:
#  torna como condicional a condição de ser bem sucedido. 
# lembrar que códigos na "coluna" 200 se remete a sucesso no recurso

    data = requests.json() #transforma os dados extraidos para .json
    with open('nasa_apod_data.json', 'w') as json_file:
        #passa como parametro a formatação desejada
        json.dump(data, json_file, indent=4)
        print('Dados salvos com sucesso em um arquivo json')
else:
    print('Erro na solicitação:', requests.status_code)
    # caso não percorra o caminho corretamente ele traz uma mensagem de erro apresentando o devido erro



    