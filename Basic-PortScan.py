# Importando o Socket
import socket


def portscan():  # nesta linha eu criei uma funçao para o portscan
    for porta in range(0,
                       1024):  # Nesta linha o valor da porta ira variar entre 0 ate 1023 e encrementando sempre +1, enquanto a máquina não chegar até o ultimo valor definido no range, o laço de repetiçao ira persistir.
        obj_socket = socket.socket(socket.AF_INET,
                                   socket.SOCK_STREAM)  # socket.AF_INET ira receber o valor do IP e o valor da porta pois se trata de uma tupla, socket.SOCK_STREAM ira definir o tipo de conexão como TCP e ambas as variaveís irão ficar guardadas em outra variável OBJ_SOCKET
        socket.setdefaulttimeout(
            0.5)  # Nesta linha eu defino que o tempo maximo em que o socket ira ficar esperando pela resposta da porta que é de 0.5 segundos.
        if (obj_socket.connect_ex((host,
                                   porta)) == 0):  # para a variavel obj_socket passei  a funçao connect_ex e passei o valor do endereço de ip e da porta lógica para a variavel obj_socket, caso a resposta for igual a 0 isso significa que uma conexão foi estabelecida ou que a porta esta aberta.
            print("[+] PORTA", porta, "esta aberta.")  # exibindo uma  mensagem caso a porta esteja aberta
        else:
            print("[+] PORTA", porta,
                  "esta fechada.")  # qualquer resposta diferente de 0 irá aparecer a mensagem de que a porta esta fechada.


print(
    " ## Iniciando o PortScan ## \n ## Este PortScan é util para escanear um range de portas sendo assim você irá inserir a porta inicial e a porta final nas quais o PortScan irá analisar.")
host = input("Digite o endereço: ")  # solicitando o IP do servidor
print("RM 95195 - JOSE LUCAS RAMOS DE LIMA - FIAP DEFESA CIBERNÉTICA ")
portscan()  # chamando a função portscan()
