## Programa de Automação básico utilizando Telnetlib.
import getpass #essa biblioteca pede um input do usuario e a esconde no CMD
import telnetlib
## Coletando endereço do servidor e as credenciais
servidores = "XXX.XXX.XXX.XXX"
usuarios = input("Usuario TELNET: ")
senha = getpass.getpass()
## Realizando a conexão através do método Telnet e passando o endereço do servidor como Paramêtro
tn = telnetlib.Telnet(HOST)
##o método read_until irá fazer exatamente o que a tradução literal dele significa, ele irá ler todos os dados somente até a string que foi inserida, assim que encontrar ele irá executar a próxima linha.
tn.read_until(b"Username: ")
##escrevendo a credencial usuário e codificando-a em formato ASCII e dando enter para enviar as credenciais de usuario
tn.write(usuarios.encode('ascii') + b"\n")
if senha: 
    tn.read_until(b"Password: ") # quando encontrar a string Password, ele irá enviar as credenciais de password
    tn.write(senha.encode('ascii') + b"\n")
## após estabelecer a conexão com o Switch/equipamento é só utilizar os campos abaixos
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")
## exibindo os dados retornados
print(tn.read_all().decode('ascii'))