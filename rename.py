import os

carpeta = "C:\\Github\\Plan-Comun\\Datasets\\Bottle"
archivos = os.listdir(carpeta)
counter = 0
for archivo in archivos:
    counter += 1
    print(archivo[-4:], counter)
    os.rename(carpeta+"\\" + archivo, carpeta+"\\"+"Plastic"+str(counter)+archivo[-4:])