
import subprocess
from bloquear_ip import bloquear_ip

ruta_log = "/var/log/auth/log" # este cambiar por /var/log/secure porque ese usa el centos
resultado = subprocess.run(['bash', './prueba.sh']) # ejecuto el script en bash
f = open("prueba.txt","r") # abro el archivo que me crea el script hecho en bash
ip_intentos = {} # un diccionario con el ip y los intentos de ingreso
for line in f:
    ip = line.split()[10]
    if ip in ip_intentos: 
        ip_intentos[ip] += 1
        if ip_intentos[ip] == 10:
            print('la ip '+ip+ ' se va a bloquear porque intento muchas veces')
            bloquear_ip(ip)
    else:
        ip_intentos[ip] = 1
#print(ip_intentos) te muestra cuantas veces intento cada ip






    