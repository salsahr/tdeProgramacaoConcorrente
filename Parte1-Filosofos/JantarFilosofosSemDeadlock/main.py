import threading
from filosofos import Filosofos

N = 5

def main():
    garfo = [None] * N

    for i in range(N):
        garfo[i] = threading.Semaphore(1)

    for i in range(N):
        esquerda = garfo[i]
        direita = garfo [(i+1)%N]

        if i == N - 1:
            f = Filosofos(i, direita, esquerda)
        else:
            f = Filosofos(i, esquerda, direita)

        f.start()

if __name__ == "__main__":
    main()