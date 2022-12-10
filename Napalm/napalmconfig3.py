#Este exemplo é do curso Python Network Programming for Network Engineers
# O código abaixo é para criar uma conexão
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()
print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.cfg')
#Nas próximas linhas é então feita uma verificação se existe uma ACL, caso não existir é então criada uma.
diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No ACL changes required.')
    iosvl2.discard_config()
# é feito uma verificação se há alguma configuração OSPF e caso não houver também é criada uma
iosvl2.load_merge_candidate(filename='ospf1.cfg')
diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No OSPF changes required.')
    iosvl2.discard_config()

iosvl2.close()
