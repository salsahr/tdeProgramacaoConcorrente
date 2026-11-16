import threading
import time

class Filosofos(threading.Thread):
    def __init__(filosofo, id, garfo_esquerdo, garfo_direito):
        super().__init__()
        filosofo.id = id
        filosofo.garfo_esquerdo = garfo_esquerdo
        filosofo.garfo_direito = garfo_direito

    def run(filosofo):
        while True:
            filosofo.pensar()
            filosofo.ficar_com_fome()
            filosofo.pegar_garfo_esquerdo()
            time.sleep(1)
            filosofo.pegar_garfo_direito()
            filosofo.comer()
            filosofo.devolver_garfos()


    def pensar(filosofo):
        print(f"Filosofo {filosofo.id} esta pensando")
        time.sleep(1)

    def ficar_com_fome(filosofo):
        print(f"Filosofo {filosofo.id} esta com fome")

    def pegar_garfo_esquerdo(filosofo):
        filosofo.garfo_esquerdo.acquire()
        print(f"Filosofo {filosofo.id} pegou o garfo esquerdo")

    def pegar_garfo_direito(filosofo):
        filosofo.garfo_direito.acquire()
        print (f"Filosofo {filosofo.id} pegou garfo direito")

    def comer(filosofo):
        print(f"Filosofo {filosofo.id} esta comendo")
        time.sleep(1)

    def devolver_garfos(filosofo):
        filosofo.garfo_esquerdo.release()
        filosofo.garfo_direito.release()
        print(f"Filosofo {filosofo.id} soltou os garfos")
