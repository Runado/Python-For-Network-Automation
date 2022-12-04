# a idéia desse programa era gerar uma requisição e automatizar uma rotina no ERP do meu antigo trabalho como Help-Desk.

import requests #biblioteca para forjar a requisição HTTP
from bs4 import BeautifulSoup #BeatifulSoup para realizar o WebScrap

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
# abaixo o Payload com o usuário e senha do ERP
login_data = {
    'data[User][login]': 'Usuario  de login no ERP',
    'data[User][password2]': 'Senha de Login no ERP',
    'form id': 'UserLoginForm'
}

with requests.Session() as s: # essa linha é só pra chamar o método através da letra s, facilitando o entendimento.
    url = 'https://erp.webbyinternet.com.br/users/login' # Url do ERP
    r = s.get(url, headers=headers) #enviando uma requisição GET para acessar a página de login do ERP
    soup = BeautifulSoup(r.content, 'html.parser') #coletando o código html da página e alocando na variável SOUP
    # enviando o payload por meio de uma requisição POST
    login_data['post'] = soup.find('form', attrs={'method': 'post'})['value']
    r = s.post(url, data=login_data, headers=headers)
    # após logar e receber o cookie de autenticação o código abaixo é para retornar a página inicial do ERP.
    home_page = s.get ("https://erp.webbyinternet.com.br/assignments")
    mostrai = BeautifulSoup(home_page.content, 'html.parser')
    print(mostrai)