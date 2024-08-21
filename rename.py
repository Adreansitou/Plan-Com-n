import os

carpeta = "C:\\Github\\Plan-Comun\\Datasets\\Bottle"
archivos = os.listdir(carpeta)
counter = 0
for archivo in archivos:
    counter += 1
    print(archivo[-4:], counter)
    if counter < 10:
        os.rename(carpeta+"\\" + archivo, carpeta+"\\"+"Plastic"+"00"+str(counter)+archivo[-4:])
    elif counter < 100:
        os.rename(carpeta+"\\" + archivo, carpeta+"\\"+"Plastic"+"0"+str(counter)+archivo[-4:])
    else:
        os.rename(carpeta+"\\" + archivo, carpeta+"\\"+"Plastic"+str(counter)+archivo[-4:])