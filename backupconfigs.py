import getpass
import telnetlib
##coletando as credenciais
user = input('Insira o Usuario Telnet: ')
password = getpass.getpass()
# arquivo onde ficará os ip's dos servidores
f = open('myswitches')
# loop que irá percorrer os ip's, realizar as conexões, executar os comandos e salvar.
for IP in f:
    IP=IP.strip()
    print ('Coletando as informações do Switch: ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    #as linhas acimas são para estabelecer a conexão via Telnet e realizar a autenticação.
    #setando o terminal lenght como 0 para durante a coleta de dados não pedir interação do usuário.
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b'exit\n')
    # as linhas abaixo coletar o output e salvar na variável saida, em seguida criar um arquivo txt e gravar os dados no output em formato ASCII

    saida = tn.read_all()
    salvaroutput =  open("switch" + HOST, "w")
    salvaroutput.write(saida.decode('ascii'))
    salvaroutput.write("\n")
    salvaroutput.close
