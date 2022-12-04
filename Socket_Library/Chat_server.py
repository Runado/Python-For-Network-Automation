## Aplicação SERVIDORA


from socket  import * #importando * todas funções no modulo para não ter que ficar chamando

servidor="127.0.0.1"
porta  = 443

obj_socket  = socket(AF_INET, SOCK_STREAM) # AF_INET irá receber o IP ou o HOSTNAME(DOMINIO) e o SOCK_STREAM irá definir que iremos utilizar o protocolo TCP
obj_socket.bind((servidor, porta)) # irá bindar os valores dessas variaveis no obj_socket,   servidor = AF_INET e  porta = SOCK_STREAM
obj_socket.listen(2) #irá ficar aguardando a conexão de dois clientes e aceitará no maximo duas conexões simulteneas

print("Aguardando o  cliente .... ")

while True: #loop
  con, cliente = obj_socket.accept() #caso alguem faça a conexão nesse servidor acima, irá   retornar uma tupla.
  print ("Conectado com: ", cliente) # mensagem que irá aparecer assim que alguem se conectar
  while True:
    msg_recebida = str(con.recv(1024)) # metodo recv seria o receive para receber a mensagem em  tamanhos de pacotes de até 1024 bytes que serão convertidas em uma string
    print ("Recebemos: ", msg_recebida) # exibindo a mensagem
    msg_enviada = b'Ola cliente' #respondendo a mensagem
    con.send(msg_enviada) #utilizamos o objeto con junto com  o metodo send para enviar a mensagem ola cliente.
    break

con.close()