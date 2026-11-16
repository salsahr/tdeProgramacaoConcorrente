import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread1():
    LOCK_A.acquire()
    print("T1 pegou LOCK_A")
    time.sleep(0.5)
    
    print("T1 aguardando LOCK_B")
    LOCK_B.acquire()
    print("T1 pegou LOCK_B")
    print("T1 concluiu")
    
    LOCK_B.release()
    LOCK_A.release()

def thread2():
    LOCK_B.acquire()
    print("T2 pegou LOCK_B")
    time.sleep(0.5)
    
    print("T2 aguardando LOCK_A")
    LOCK_A.acquire()
    print("T2 pegou LOCK_A")
    print("T2 concluiu")
    
    LOCK_A.release()
    LOCK_B.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print("FIM")