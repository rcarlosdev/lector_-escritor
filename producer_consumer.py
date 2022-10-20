import time
import queue
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

"""
Problema productor-consumidor
El programa describe dos procesos, productor y consumidor,
ambos comparten un buffer de tamaño finito.
La tarea del productor es generar un producto, almacenarlo y comenzar nuevamente;
mientras que el consumidor toma (simultáneamente) productos uno a uno.
El problema consiste en que el productor no añada más productos que la capacidad del buffer
y que el consumidor no intente tomar un producto si el buffer está vacío.
"""

queue = queue.Queue(maxsize=10)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, 52, 53, 54, 55]


def producer():
    while items:
        if not queue.full():
          item = items.pop(0)
          queue.put(item)
          logging.debug('Producido:  {}'.format(item))
          time.sleep(random.randint(1, 3))
          if queue.full():
            logging.debug('Buffer lleno')
          if items == []:
            logging.debug('No hay más productos')

def consumer():
    while True:
        if not queue.empty():
          item = queue.get()
          queue.task_done()
          logging.info(f'Consumido: {item}')
          time_to_sleep = random.randint(1, 4)
          time.sleep(time_to_sleep)
          if queue.empty():
            logging.info('Buffer vacío')
            break


if __name__ == '__main__':
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()
