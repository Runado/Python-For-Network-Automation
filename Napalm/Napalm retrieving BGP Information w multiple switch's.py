import json
from napalm import get_network_driver
bgplist = ['localhost','192.168.1.1','192.168.1.2']

for ip in bgplist: # loop para conectar e retornar as informações de BGP  de cada Switch
        print("Conectando ao IP: " + str(ip))
        driver = get_network_driver('ios')
        switch = driver(ip,'jose','teste') #conexao ao switch
        switch.open()
        bgp_neighbors = switch.get_bgp_neighbors()
        print(json.dumps(bgp_neighbors, indent=4))
        switch.close()