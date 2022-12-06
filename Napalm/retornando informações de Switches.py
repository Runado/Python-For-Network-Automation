from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver('localhost','jose','teste') #hostname, username, password, timeout=X, optional_args=None
ios.open()
ios_output = ios.get_facts() # Função retorna uptime - Uptime of the device in seconds.
#vendor - Manufacturer of the device.
#model - Device model.
#hostname - Hostname of the device
#fqdn - Fqdn of the device
#os_version - String with the OS version running on the device.
#serial_number - Serial number of the device
#interface_list - List of the interfaces of the device
print(ios_output)