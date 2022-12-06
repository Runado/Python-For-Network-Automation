import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver('localhost','jose','teste') #hostname, username, password, timeout=X, optional_args=None
ios.open()
ios_output = ios.get_facts()
print(json.dumps(ios_output, indent=4))
 # Função retorna uptime - Uptime of the device in seconds.
#vendor - Manufacturer of the device.
#model - Device model.
#hostname - Hostname of the device
#fqdn - Fqdn of the device
#os_version - String with the OS version running on the device.
#serial_number - Serial number of the device
#interface_list - List of the interfaces of the device
print(ios_output)

## Formatando a saída.
ios_output = ios.get_interfaces() # retorna as interfaces
print(json.dumps(ios_output, sort_keys=True, indent=4)) # função sort_keys é para organizar a saída
ios_output = ios.get_interfaces_counters() # retorna as interfaces com mais informações
print(json.dumps(ios_output, sort_keys=True, indent=4))
ios_output = ios.get_mac_address_table() # retorna a tabela de MAC dos equipamentos
print(json.dumps(ios_output,  indent=4))
ios_output = ios.get_arp_table() # retorna a tabela de ARP dos equipamentos
print(json.dumps(ios_output,  indent=4))
ios_output = ios.ping('google.com') # enviando um ping para o google.com e retornando os dados
print(json.dumps(ios_output,  indent=4))
