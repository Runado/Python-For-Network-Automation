from netmiko import ConnectHandler
## neste dicionario irá ficar as credenciais de acesso ao switch's
switch1 = {
    'device_type': 'cisco_ios',
    'ip': 'localhost',
    'username': 'jose',
    'password': 'teste'
}
switch2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'jose',
    'password': 'teste'
}
switches = [switch1, switch2]
for switch in switches:
    conexao = ConnectHandler(**switch) #Iniciando a conexão por meio do método ConnectHandler e passando as credenciais.
    saida = conexao.send_command('show ip int brief') # comando para mostrar as interfaces do switch
    print (saida)

    cmd = ['enable','int loop 0', 'ip address 1.1.1.1 255.255.255.0'] #lista com comandos a serem enviados, nesta linha estamos setando um IP na Loopback0
    saida = conexao.send_config_set(cmd) #este método irá enviar os comandos de uma lista ou arquivo de forma respectiva ou seja um por vez, ideal para passar comandos que serão executados sucessivamente.
    print (saida)
## Loop para criar vlan's
    for n in range (2,21):
        print ("Criando VLAN " + str(n))
        vlan = ['VLAN ' + str(n), 'name Python_VLAN ' + str(n)]
        output = vlan.send_config_set(vlan)
        print (output)
