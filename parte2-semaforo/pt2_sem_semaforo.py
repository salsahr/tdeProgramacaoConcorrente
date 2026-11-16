import time
import threading

T = 8
M = 200000
contador = 0

def tarefa():
    global contador
    for _ in range(M):
        temp = contador
        time.sleep(0)
        contador = temp + 1

tempo_comeco = time.time()
threads = []

for _ in range(T):
    thread = threading.Thread(target=tarefa)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

tempo_fim = time.time()
tempo = tempo_fim - tempo_comeco

print("Esperado: ", T * M, " Obtido: ",contador, "Perdidos: ", T * M - contador, "Tempo: ",tempo)