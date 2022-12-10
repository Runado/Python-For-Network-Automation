#Exemplo de multiplas configurações utilizando NAPALM

import json
from napalm import get_network_driver
#Lista dos switch's
devicelist = ["localhost",
           '192.168.1.1'
           ]
# Esse laço de repetição irá percorrer a lista verificando se há uma ACL e se há uma configuração OSPF ou aplicando as configs.

for ip_address in devicelist:
    #realizando a conexão.
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'david', 'cisco')
    iosv.open()
    #arquivo com a configuração da Access Control List aplicando as configs
    iosv.load_merge_candidate(filename='ACL1.cfg')
    diffs = iosv.compare_config()
    #verificando se há alguma configuração, caso não houver ele estará aplicando.
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required.')
        iosv.discard_config()
    #aplicando as configurações de OSPF
    iosv.load_merge_candidate(filename='ospf1.cfg')
    #Verificando se há alguma config, caso não houver será comitado os comandos presentes no arquivo OSPF1.
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
    	print('No OSPF changes required.')
    	iosv.discard_config()

    iosv.close()




