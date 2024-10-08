import os
import pywhatkit
import time
numero = "+xx xxxxxxxx"

imagepath = "image path mesmo"

os.system('cls')
contador = 0

while contador < 5:
    pywhatkit.sendwhats_image(numero, imagepath,"joao dolinsky hasum",10,True)

    time.sleep(5)
    contador += 1



