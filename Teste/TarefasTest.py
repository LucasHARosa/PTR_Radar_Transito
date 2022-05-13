from threading import Thread
import time
import MonitorTimes
import sim
import numpy as np
import random

clientID = 0
Camera = 0
resolucao = []
imagem = []
estatusBt = []


def setInicio(ID, camera, bt):
    global clientID
    global Camera
    global resolucao
    global imagem
    global Bt
    global estatusBt
    clientID = ID
    Bt = bt
    Camera = camera
    erro, resolucao, imagem = sim.simxGetVisionSensorImage(clientID, Camera, 0, sim.simx_opmode_streaming)
    time.sleep(1)
    estatusBt = sim.simxReadProximitySensor(clientID, Bt, sim.simx_opmode_streaming)


class falha(Thread):

    def __init__(self,tempos):
        Thread.__init__(self)
        self.tempos = tempos

    def run(self):
        t = time.time()
        sim.simxAddStatusbarMessage(clientID, 'FALHA', sim.simx_opmode_oneshot_wait)
        tf = time.time()
        self.tempos.append(tf - t)


# _______________________________________________________________
class verificaBt(Thread):
    def __init__(self, sem, tempos):
        Thread.__init__(self)
        self.semaforo = sem
        self.tempos = tempos

    def run(self):
        t = time.time()

        sim.simxReadProximitySensor(clientID, Bt, sim.simx_opmode_buffer)
        button = random.choice([True, False])
        print("semafor:" + str(self.semaforo) + " button :" + str(button))
        if button and self.semaforo == 0:
            self.semaforo = 1
            sim.simxAddStatusbarMessage(clientID, 'Semaforo esta Vermelho', sim.simx_opmode_oneshot_wait)
            print('Semaforo esta Vermelho')
            time.sleep(0.01)  # tempo para alterar o estado
            MonitorTimes.alteraSemaforo(self.semaforo)
        else:
            if self.semaforo == 1:
                self.semaforo = 0
                sim.simxAddStatusbarMessage(clientID, 'Semaforo esta Verde', sim.simx_opmode_oneshot_wait)
                print('Semaforo esta Verde')
                time.sleep(0.01)  # tempo para alterar o estado
                MonitorTimes.alteraSemaforo(self.semaforo)
        tf = time.time()
        self.tempos.append(tf - t)


# ______________________________________________________________
class Mostrar(Thread):
    def __init__(self, x, v, tempos):
        Thread.__init__(self)
        self.x = x
        self.v = v
        self.tempos = tempos

    def run(self):
        t = time.time()
        if self.x:
            sim.simxAddStatusbarMessage(clientID, 'excesso de velocidae :' + str(self.v) + 'Km/h',
                                        sim.simx_opmode_oneshot_wait)

        else:
            sim.simxAddStatusbarMessage(clientID, str(self.v) + 'Km/h', sim.simx_opmode_oneshot_wait)
        tf = time.time()
        self.tempos.append(tf - t)


# ______________________________________________________________
class AtivaCamera(Thread):

    def __init__(self, tempos):
        Thread.__init__(self)
        self.tempos = tempos
        self.Camera = Camera

    def run(self):
        t = time.time()
        global resolucao, imagem
        erro, resolucao, imagem = sim.simxGetVisionSensorImage(clientID, Camera, 0, sim.simx_opmode_buffer)
        im = np.array(imagem, dtype=np.uint8)
        im.resize([resolucao[0], resolucao[1], 3])
        tf = time.time()
        self.tempos.append(tf - t)
        print(im.shape)
        # mlp.show(im)


# ________________________________________________________________

class calculo(Thread):

    def __init__(self, tempos, temposC, temposM, temposF):
        Thread.__init__(self)
        self.tempos = tempos
        self.temposC = temposC
        self.temposM = temposM
        self.temposF = temposF

    def run(self):
        t = time.time()
        vMax = 60  # km/h
        ds = 0.5
        t1, t2, t3 = MonitorTimes.lertempos()
        v = 0

        if t1 == 0:
            if t2 == 0 or t3 == 0:
                falha(self.temposF).start()
            else:
                v = (ds / (t3 - t2)) * 3.6
        else:
            if t2 == 0:
                if t3 == 0:
                    falha(self.temposF).start()
                else:
                    v = (2 * ds / (t3 - t1)) * 3.6
            else:
                if t3 == 0:
                    v = (ds / (t2 - t1)) * 3.6
                else:
                    v1 = (ds / (t3 - t2)) * 3.6
                    v2 = (ds / (t2 - t1)) * 3.6
                    v = (v1 + v2) / 2
        if v != 0:
            if v > vMax:
                AtivaCamera(self.temposC).start()
                Mostrar(True, int(v), self.temposM).start()
            else:
                Mostrar(False, int(v), self.temposM).start()
        tf = time.time()
        self.tempos.append(tf - t)


# ______________________________________________________________
class sensor1Ativado(Thread):

    def __init__(self, tempos):
        Thread.__init__(self)
        self.tempos = tempos

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(1, t)
        tf = time.time()
        self.tempos.append(tf - t)
        #sim.simxAddStatusbarMessage(clientID, 'S1 detectado', sim.simx_opmode_oneshot_wait)
        # print('S1 detectado')


# ______________________________________________________________

class sensor2Ativado(Thread):

    def __init__(self, tempos):
        Thread.__init__(self)
        self.tempos = tempos

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(2, t)
        tf = time.time()
        self.tempos.append(abs(tf - t))
        # print('S2 detectado')
        #sim.simxAddStatusbarMessage(clientID, 'S2 detectado', sim.simx_opmode_oneshot_wait)


# ______________________________________________________________
class sensor3Ativado(Thread):

    def __init__(self, tempos):
        Thread.__init__(self)
        self.tempos = tempos

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(3, t)
        tf = time.time()
        self.tempos.append(abs(tf - t))
        # print('S3 detectado')
        #sim.simxAddStatusbarMessage(clientID, 'S3 detectado', sim.simx_opmode_oneshot_wait)
