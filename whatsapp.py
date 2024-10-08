import os
import pywhatkit
import time
numero_big = "+351 910 237 127"

imagepath = "C:/Users/T-GAMER/Pictures/leandro hassum.jfif"

os.system('cls')
contador = 0

while contador < 5:
    pywhatkit.sendwhats_image(numero_big, imagepath,"joao dolinsky hasum",10,True)

    time.sleep(5)
    contador += 1



