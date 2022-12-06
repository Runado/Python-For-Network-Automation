import json
from napalm import get_network_driver
driver = get_network_driver('ios')
conexao = driver('localhost', 'jose', 'teste')
conexao.open()

print ('Accessing localhost')
conexao.load_merge_candidate(filename='ACL1.cfg')
conexao.commit_config()
conexao.close()


