import threading


mutex = threading.RLock()
temT1 = threading.Condition(mutex)
temT2 = threading.Condition(mutex)
temT3 = threading.Condition(mutex)
TS1 = 0.0
TS2 = 0.0
TS3 = 0.0
semaforo = 0


def alteraSemaforo(sem):
    mutex.acquire()
    global semaforo
    semaforo=sem
    mutex.release()


def lerSemaforo():
    mutex.acquire()
    aux = semaforo
    mutex.release()
    return aux


def iserirTempo(i, t):
    mutex.acquire()
    if i == 1:
        global TS1
        TS1 = t
    if i == 2:
        with temT2:
            global TS2
            TS2 = t
            temT2.notify()
    if i == 3:
        with temT3:
            global TS3
            TS3 = t
            temT3.notify()
    mutex.release()



def lertempos():
    mutex.acquire()
    global TS1, TS2, TS3
    aux1 = TS1
    with temT2:
        if TS2 == 0.0:
            temT2.wait(0.3)
        aux2 = TS2
    with temT3:
        if TS3 == 0.0:
            temT3.wait(0.3)
        aux3 = TS3
    TS1 = 0.0
    TS2 = 0.0
    TS3 = 0.0
    mutex.release()
    return aux1, aux2, aux3

