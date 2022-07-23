# Le pasas una ip como string y te bloquea la ip

import subprocess

def bloquear_ip(ip):
    # Bloqueo la conexion de la ip para todo los servicios
    resultado = subprocess.run(['iptables', '-A' ,'INPUT', '-s', 
    ip, '-j','DROP'])

'''
de prueba
ip = '10.9.8.7'
bloquear_ip(ip)
'''