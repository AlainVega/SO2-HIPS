from .verificar_cambio_archivo import verificar_cambio_archivo
from pathlib import Path
import os.path
from .registrar_en_log import registrar_en_log

def verificar_binarios():
    pathlist = Path('/bin/')
    mensaje = ''
    se_cambio_alguno = False
    for path in pathlist.iterdir():
        if not os.path.isdir(path):
            if not verificar_cambio_archivo(path, '/backups/hashes/bin/' + path.name):
                se_cambio_alguno = True
                mensaje += 'El archivo: ' + str(path) + ' ha sido modificado\n'
                registrar_en_log('alarmas','cambio en /bin','',
                'El archivo: ' + str(path) + ' ha sido modificado')
    ruta_archivos = ['/etc/passwd', '/etc/group', '/etc/shadow']
    for ruta in ruta_archivos:
        if not verificar_cambio_archivo(ruta, '/backups/hashes/etc/' + ruta.split('/')[2]):
            se_cambio_alguno = True
            mensaje += 'El archivo: ' + ruta + ' ha sido modificado\n'
            registrar_en_log('alarmas','cambio en /etc','',
            'El archivo: ' + ruta + ' ha sido modificado')
    if se_cambio_alguno:
        return 'Se detecto la modificacion de:\n' + mensaje
    else:
        return 'No se detectaron cambios en los binarios, ni en el /etc/passwd, /etc/group, /etc/shadow'
        
#print(verificar_binarios())
