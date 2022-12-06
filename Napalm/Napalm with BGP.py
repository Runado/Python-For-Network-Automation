import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver('localhost','jose', 'teste') #(hostname, username, password)
ios.open() # conectando
ios_output = ios.get_facts() # retornando informações básicas do switch
print(json.dumps(bgp_neighbors, indent=4))
bgp_neighbors = ios.get_bgp_neighbors()# retornando os BGP neighbors
print(json.dumps(bgp_neighbors, indent=4))