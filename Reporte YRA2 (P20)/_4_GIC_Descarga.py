import os
import requests
from datetime import datetime
import shutil


def Descargar_GIC(): 

    print("==============================================================================================================")
    print("====INICIALIZACION DE LA DESCARGA DEL ARCHIVO GIC")
    print("==============================================================================================================\n")

    print("========================================================================")
    print("----Descargando Archivo GIC")
    print("========================================================================\n")

    # ----Define la variable url que contiene la dirección URL del archivo que se va a descargar
    url = "http://dataq-prod.int.net.nokia.com:7780/pls/apex/f?p=115:8::CSV::::"    

    fecha= "{:%Y_%m_%d}".format(datetime.now())
    
    # ----Define la variable filename que contiene el nombre que se le dará al archivo descargado en el sistema local.
    filename_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'YRA2') + "\\F&C GIC - SIG PC List - " + fecha + ".csv"
    filename = "F&C GIC - SIG PC List_" + fecha + ".csv"

    # ----Te avisa si ya descargo el archivo
    response = requests.get(url)

    print("========================================================================")
    print("----Archivo GIC descargado en la Carpeta YRA2 del Escritorio")
    print("----"+filename)
    print("========================================================================\n")

    # ----Verifica si la carpeta "mi_carpeta" existe en el sistema de archivos utilizando la función "os.path.exists()". Si la carpeta no existe, se crea utilizando la función "os.makedirs()".
    directorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\YRA2"
    try:
       os.stat(directorio)
    except:
       os.mkdir(directorio)

    # ----Check if file already exists
    if os.path.isdir(filename_path):
        print("========================================================================")
        print('----'+filename, '____ Exists in the destination path!')
        print("========================================================================\n")
        shutil.rmtree(filename_path)
    
    elif os.path.isfile(filename_path):
        os.remove(filename_path)
        print("========================================================================")
        print('----'+filename, '____ Deleted in', 'YRA2', 'becuase is duplicate')
        print("========================================================================\n")

    with open(filename_path, "wb") as f:
        f.write(response.content)

    print("==============================================================================================================")
    print("====FINALIZACION DE LA DESCARGA DEL ARCHIVO GIC")
    print("==============================================================================================================\n")

    

#       """""""""En dado caso que quiera ejecutarlo aca en el archivo:""""""""""
#Descargar_GIC()