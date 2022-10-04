from operator import contains
import threading as th
import time

def paralelo():
    global contador
    global conti
    
    contador = 0    
    conti = True
    
    while(conti):        
        print("Hilo paralelo ejecutandose ", contador)
        time.sleep(1)
        contador = contador + 1
        
    
print("Inicio main.")
hilo = th.Thread(target=paralelo)
hilo.start()

continuar = True
while continuar:
    dato = input("Digita a para detener el programa:  ")
    if dato=="a":
        print(contador)
    elif dato == "z":
        continuar = False
        conti = False
    else:
        print(dato)

        
print("Fin main")