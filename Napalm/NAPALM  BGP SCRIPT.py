import json
from napalm import get_network_driver

driver = get_network_driver('ios')
switch = driver(localhost,'jose','teste') #conexao ao switch
switch.open()
bgp_neighbors = switch.get_bgp_neighbors()
print(json.dumps(bgp_neighbors, indent=4))
switch.close()