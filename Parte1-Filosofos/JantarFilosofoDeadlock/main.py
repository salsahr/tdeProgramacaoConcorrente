import threading

from filosofos import Filosofos

N = 5

def main():
    garfo = [None] * N

    for i in range(N):
        garfo[i] = threading.Semaphore(1)

    for i in range(N):
        f = Filosofos(i, garfo[i], garfo[(i+1)%N])
        f.start()


if __name__ == "__main__":
    main()
