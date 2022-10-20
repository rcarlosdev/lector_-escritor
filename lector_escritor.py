import threading
import time
import random

lectores = 0
mutex = threading.Semaphore(1)
bd = threading.Semaphore(1)
i = 0


def leyendo():
    print('\033Leyendo')
    time.sleep(random.randint(1, 10))
    print('\033Dejando de leer')


def escribiendo():
    print('\033Escribiendo')
    time.sleep(random.randint(1, 10))
    print('\033Dejando de escribir')


# PRIORIDAD AL LECTOR
def lector():
    global lectores
    mutex.acquire()
    lectores = lectores + 1
    if lectores == 1:
        bd.acquire()
    mutex.release()

    leyendo()

    mutex.acquire()
    lectores = lectores - 1
    if lectores == 0:
        bd.release()
    mutex.release()


def escritor():
    bd.acquire()  # wait
    escribiendo()
    bd.release()


###############################MAIN############################
ingresar_orden = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]  # 0 - lector y 1 - escritor
lista = []

for persona in (ingresar_orden):
    if persona == 0:
        lista.append(threading.Thread(target=lector))
    elif persona == 1:
        lista.append(threading.Thread(target=escritor))
    else:
        print("ERROR---------------")
        break
    i = i + 1


for hilo in (lista):
    hilo.start()
