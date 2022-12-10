import json
from napalm import get_network_driver
#Criando a conexão
driver = get_network_driver("ios")
switch = driver('localhost','jose', 'teste')
switch.open()

print("Acessando o Switch ")
# Será enviado o comando que está contido na ACL1 porém sem commit.
switch.load_merge_candidate(filename="ACL1.txt")


#nas linhas abaixo é printado as configurações de cada switch e em seguida é feito uma validação se há alguma ACL criada, caso não houver então o commit é feito e uma nova configuração é aplicada.
verifica = switch.compare_config() #este comando mostra a saída das configurações do switch
if len(verifica) > 0:
    print(verifica)
    switch.commit_config()
else:
    print("Este Switch já tem uma ACL")
    switch.discard_config()
switch.close()
