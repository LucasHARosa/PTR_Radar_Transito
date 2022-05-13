from threading import Thread
import time
import MonitorTimes
import camera
import sim
import numpy as np
import matplotlib.pyplot as mlp

clientID = 0
Camera = 0


def setInicio(ID,camera):
    global clientID
    global Camera
    clientID = ID
    Camera = camera
    


class falha(Thread):

    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        t = time.time()
        print('FALHA')
        sim.simxAddStatusbarMessage(clientID, 'FALHA', sim.simx_opmode_oneshot_wait)


# _______________________________________________________________
class verificaBt(Thread):
    def __init__(self, S):
        Thread.__init__(self)
        self.semaforo = S

    def run(self):
        self.button = sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_buffer)
        sim.simxAddStatusbarMessage(clientID, 'Verifica se o botao foi apertado', sim.simx_opmode_oneshot_wait)
        if ((self.button == (0, 1)) and (self.semaforo == 0)):
            MonitorTimes.alteraSemaforo(1)
            time.sleep(0.01)  # tempo para alterar o estado
            sim.simxAddStatusbarMessage(clientID, 'SEMAFORO ESTA VERMELHO', sim.simx_opmode_oneshot_wait)

        if ((self.button == (0, 0)) and (self.semaforo == 1)):
            MonitorTimes.alteraSemaforo(0)
            time.sleep(0.01)  # tempo para alterar o estado
            sim.simxAddStatusbarMessage(clientID, 'SEMAFORO ESTA VERDE', sim.simx_opmode_oneshot_wait)


# ______________________________________________________________
class Mostrar(Thread):
    def __init__(self, x, v):
        Thread.__init__(self)
        self.x = x
        self.v = v

    def run(self):
        if self.x:
            print ('excesso de velocidae :' + str(self.v) + 'Km/h')
            sim.simxAddStatusbarMessage(clientID, 'Excesso de velocidae :' + str(self.v) + 'Km/h',
                                        sim.simx_opmode_oneshot_wait)
        else:
            print(str(self.v) + 'Km/h')
            sim.simxAddStatusbarMessage(clientID, str(self.v) + 'Km/h', sim.simx_opmode_oneshot_wait)


# ______________________________________________________________
class AtivaCamera(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        sim.simxAddStatusbarMessage(clientID, 'CARRO FOTOGRAFADO', sim.simx_opmode_oneshot_wait)
        camera.tirafoto(Camera,clientID)
        #Comentado pois dependendo da IDE não funciona
        
        #erro,resolution,arrayimagem = sim.simxGetVisionSensorImage(clientID,Camera,0,sim.simx_opmode_oneshot_wait)
        #im = np.array(arrayimagem, dtype=np.uint8)
        #im.resize([resolution[0], resolution[1], 3])
        #mlp.imshow(im,origin='lower')
        #mlp.show()
    


# ________________________________________________________________

class calculo(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        vMax = 30  # km/h
        ds = 0.5  # m
        t1, t2, t3 = MonitorTimes.lertempos()
        print("t2-t1: " + str(t2 - t1))
        print("t3-t2: " + str(t3 - t2))
        v = 0

        if t1 == 0:
            if t2 == 2 or t3 == 0:
                falha().start()
            else:
                v = (ds / (t3 - t2)) * 3.6
        else:
            if t2 == 0:
                if t3 == 0:
                    falha().start()
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
                AtivaCamera().start()
                Mostrar(True, int(v)).start()         
            else:
                Mostrar(False, int(v)).start()


# ______________________________________________________________
class sensor1Ativado(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(1, t)
        sim.simxAddStatusbarMessage(clientID, 'S1 detectado', sim.simx_opmode_oneshot_wait)


# ______________________________________________________________

class sensor2Ativado(Thread):

    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(2, t)
        sim.simxAddStatusbarMessage(clientID, 'S2 detectado', sim.simx_opmode_oneshot_wait)


# ______________________________________________________________
class sensor3Ativado(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def run(self):
        t = time.time()
        MonitorTimes.iserirTempo(3, t)
        sim.simxAddStatusbarMessage(clientID, 'S3 detectado', sim.simx_opmode_oneshot_wait)
