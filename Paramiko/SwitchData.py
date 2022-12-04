import paramiko
import time
print('----------------------------  Programa para coletar dados dos Switch --------------------------------------')
huaweiserver = ["Servidores"]
usuario = "usuario"
senha = "senha"
lista = []


def comando(servidoreshw, usuario, senha, listcommand, cmdhuawei):
    print(servidoreshw)
    print(cmdhuawei)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=servidoreshw, username=usuario, password=senha, port="SSH PORT") # conectando aos switch
    stdin, stdout, stderr = ssh.exec_command((cmdhuawei)) # executando o comando.
    time.sleep(1)
    stdin.close() # fechando a conexão SSH
    kct = stdout.read().decode('utf-8') # decodificando a saída do comando anterior
    print(kct) # printando na tela para mostrar pro usuário
       # no for abaixo o programa irá gravar na lista a saída do comando e formatar corretamente
    for linhas in kct:
        formatando = linhas.replace('\n', '')
        listcommand.append(formatando)
        print (linhas)
    ssh.close() # assim que o comando inserido for executados em todos os switch's da lista a execução irá terminar.

# este while é para simular simular um terminal do switch pedindo os comandos que serão executados no switch's que estão na lista para o usuário
while True:
    cmd = input("Huawei# ")
    if cmd == "exit":
        break
    for servidores in huaweiserver:
        comando(servidores, usuario, senha, lista, cmd)

# gravando os dados de saída em um arquivo
with open("saida.txt", "w") as arquivo:
    for saidacommand in lista:
        arquivo.write(saidacommand)