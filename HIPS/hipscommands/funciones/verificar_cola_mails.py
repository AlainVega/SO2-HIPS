import os
from .registrar_en_log import registrar_en_log

def verificar_cola_correo():
    cmd = "mailq"
    resultado_cmd = os.popen(cmd).read()
    mensaje = ''
    if "queue is empty" in resultado_cmd:
        #print("La cola esta vacia")
        mensaje += "La cola esta vacia\n"
    else:
        resultado = resultado_cmd.splitlines()
    mail_queue = resultado_cmd.splitlines()
    if len(mail_queue) > 5: # elegir una cantidad adecuada
        #print("Se encontraron muchos mails en la cola, se aviso al administrador")
        mensaje += "Se encontraron muchos mails (" + str(len(mail_queue)) + ") en la cola, se aviso al administrador\n"
        registrar_en_log('alarmas', 'cola correo','',
        'Se detectaron muchos correos en la cola')
        # avisar al admin
    else:
        #print('no se encontraron muchos mails en la cola')
        mensaje += "No se encontraron muchos mails en la cola\n"
    return mensaje

#print(verificar_cola_correo())