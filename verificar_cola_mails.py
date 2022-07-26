import os

def check_cola_correo():
    lista_msg = []
    cmd = "mailq"
    resultado_cmd = os.popen(cmd).read()
    
    if "queue is empty" in resultado_cmd:
        print("La cola esta vacia")
        msg = 'La cola esta vacia'
       #listamsg.append(HTML(msg))
    else:
        resultado = resultado_cmd.splitlines()

    mail_queue = resultado_cmd.splitlines()
    
    if len(mail_queue) > 5: # elegir una cantidad adecuada
        print("Se encontraron muchos mails en la cola, se aviso al administrador")
        msg = "Se encontraron muchos mails en la cola, se aviso al administrador"
        #listamsg.append(HTML(msg))
        #escribir_log(alarmas_o_prevencion='alarmas',
                    #tipo_alarma='COLA_MAIL',
                    #motivo='Se detecto muchos mails en la cola')
        #func_enviar_mail(tipo_alerta='ALERTA!', asunto='MAIL QUEUE', cuerpo=f'se encontraron {len(mail_queue)} mails en la cola')

    else:
        print('no se encontraron muchos mails en la cola')
        msg = 'no se encontraron muchos mails en la cola'
        #listamsg.append(HTML(msg))
    return lista_msg

check_cola_correo()