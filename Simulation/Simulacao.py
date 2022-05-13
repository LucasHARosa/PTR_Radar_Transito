# simRemoteApi.start(19999)

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('--------------------------------------------------------------\n')


import time
import MonitorTimes
import Tarefas
import camera
import matplotlib.pyplot as mlp
import numpy as np
from threading import Thread


# -----------------------------------START----------------------------
print ('Program started')
sim.simxFinish(-1)  # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:
    print ('Connected to remote API server')
    sim.simxAddStatusbarMessage(clientID, 'conectado a API...', sim.simx_opmode_oneshot)
    erro, S1 = sim.simxGetObjectHandle(clientID, 'S1', sim.simx_opmode_oneshot_wait)
    erro, S2 = sim.simxGetObjectHandle(clientID, 'S2', sim.simx_opmode_oneshot_wait)
    erro, S3 = sim.simxGetObjectHandle(clientID, 'S3', sim.simx_opmode_oneshot_wait)
    erro, Camera = sim.simxGetObjectHandle(clientID, 'Camera', sim.simx_opmode_oneshot_wait)

    estatusS1 = sim.simxReadProximitySensor(clientID, S1, sim.simx_opmode_streaming)
    estatusS2 = sim.simxReadProximitySensor(clientID, S2, sim.simx_opmode_streaming)
    estatusS3 = sim.simxReadProximitySensor(clientID, S3, sim.simx_opmode_streaming)
    button = sim.simxGetInt32Signal(clientID, "myButton", sim.simx_opmode_streaming)
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flagCalculo = False
    flagCamera = False
    time.sleep(2)
    Tarefas.setInicio(clientID,Camera)  # Passa o clinetID e o Handle da camera para a classe tarefas
    thc = Tarefas.calculo()
    tempoinicio = time.time()
    semaforo = 0
    sim.simxAddStatusbarMessage(clientID, 'SEMAFORO ESTA VERDE', sim.simx_opmode_oneshot_wait)
    # -------------------------------Fim da inicializacao ------------------------------------------------
    while True:

        estatusS1 = sim.simxReadProximitySensor(clientID, S1, sim.simx_opmode_buffer)
        if (semaforo == 0) and estatusS1[1]:
            if flag1 == 0:
                print("S1 detect")
                Tarefas.sensor1Ativado().start()
                flag1 = 1
        elif semaforo == 1 and estatusS1[1]:
            if not flagCamera:
                sim.simxAddStatusbarMessage(clientID, "Multa por sinal vermelho", sim.simx_opmode_oneshot_wait)
                Tarefas.AtivaCamera().start()
                camera.tirafoto(Camera,clientID)
                flagCamera = True
        else:
            if flag1 == 1:
                flag1 = 0
                flagCamera = False

        estatusS2 = sim.simxReadProximitySensor(clientID, S2, sim.simx_opmode_buffer)
        if estatusS2[1]:
            if flag2 == 0:
                print("S2 detect")
                if semaforo == 0:
                    Tarefas.sensor2Ativado().start()
                    if not flagCalculo:
                        Tarefas.calculo().start()
                        flagCalculo = True
                else:
                    if not flagCamera:
                        sim.simxAddStatusbarMessage(clientID, "multa por sinal vermelho", sim.simx_opmode_oneshot_wait)
                        Tarefas.AtivaCamera().start()
                        camera.tirafoto(Camera,clientID)
                        flagCamera = True
                flag2 = 1

        estatusS3 = sim.simxReadProximitySensor(clientID, S3, sim.simx_opmode_buffer)
        if estatusS3[1]:
            if flag3 == 0:
                print("S3 detect")
                if semaforo == 0:
                    Tarefas.sensor3Ativado().start()
                    if not flagCalculo:
                        Tarefas.calculo().start()
                        flagCalculo = True
                else:
                    if not flagCamera:
                        sim.simxAddStatusbarMessage(clientID, "Multa por sinal vermelho", sim.simx_opmode_oneshot_wait)
                        Tarefas.AtivaCamera().start()
                        camera.tirafoto(Camera,clientID)
                        flagCamera = True
                flag3 = 1
        else:
            if flag3 == 1:
                flag3 = 0
                flag2 = 0
                flagCalculo = False
                flagCamera = False

        tempoVerifica = time.time()
    

        if ((tempoVerifica - tempoinicio) > 20):
            print('Verifica botao')
            Tarefas.verificaBt(semaforo)
            time.sleep(0.01)
            Tarefas.verificaBt(semaforo).start()
            time.sleep(0.1)
            tempoinicio = time.time()
            semaforo = MonitorTimes.lerSemaforo()

else:
    print ('Failed connecting to remote API server')
print ('Program ended')
