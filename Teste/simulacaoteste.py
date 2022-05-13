import MonitorTimes
import TarefasTest
import time
import sim
import random

import pandas as pd
import plotly.express as px


class Teste():
    temposVerificaBt = []
    temposMostra = []
    temposCamera = []
    temposCalculo = []
    temposS1 = []
    temposS2 = []
    temposS3 = []
    temposFalha = []

    def __init__(self):
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = 0
        self.flagC = False
        self.estatusS1 = False
        self.estatusS2 = False
        self.estatusS3 = False
        self.semaforo = 0

    def rodar(self):
        if self.estatusS1:
            if self.flag1 == 0:
                if self.semaforo == 1:
                    print("multa por sinal vermelho")
                    TarefasTest.AtivaCamera(tempos=self.temposCamera).start()
                    self.flag1 = 1
                if self.semaforo == 0:
                    TarefasTest.sensor1Ativado(tempos=self.temposS1).start()
                    # TarefasTest.calculo(tempos=self.temposCalculo, temposC=self.temposCamera,
                                        # temposM=self.temposMostra, temposF=self.temposFalha).start()
                    # self.flagC = True
                    self.flag1 = 1
        else:
            if self.flag1 == 1:
                self.flag1 = 0
                self.flagC = False

        if self.estatusS2:
            if self.flag2 == 0:
                if self.semaforo == 0:
                    TarefasTest.sensor2Ativado(tempos=self.temposS2).start()
                    if not self.flagC:
                        TarefasTest.calculo(tempos=self.temposCalculo, temposC=self.temposCamera,
                                            temposM=self.temposMostra, temposF=self.temposFalha).start()
                        self.flagC = True
                    self.flag2 = 1
        else:
            if self.flag2 == 1:
                self.flag2 = 0
                self.flagC = False

        if self.estatusS3:
            if self.flag3 == 0:
                if self.semaforo == 0:
                    TarefasTest.sensor3Ativado(tempos=self.temposS3).start()
                    if not self.flagC:
                        TarefasTest.calculo(tempos=self.temposCalculo, temposC=self.temposCamera,
                                            temposM=self.temposMostra, temposF=self.temposFalha).start()
                        self.flagC = True
                    self.flag3 = 1
        else:
            if self.flag3 == 1:
                self.flag3 = 0
                self.flagC = False

    # _________________Variantes do teste__________________________________
    def todosOK(self, t):
        self.rodar()
        self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS1(self, t):
        self.rodar()
        # self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS2(self, t):
        self.rodar()
        self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        # self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS3(self, t):
        self.rodar()
        self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        # self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS1eS2(self, t):
        self.rodar()
        # self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        # self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS1eS3(self, t):
        self.rodar()
        # self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        # self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    def perdeS2eS3(self, t):
        self.rodar()
        self.estatusS1 = True
        # print ("passou por S1")
        self.rodar()

        time.sleep(t)

        # self.estatusS2 = True
        # print ("passou por S2")
        self.rodar()

        time.sleep(t)

        # self.estatusS3 = True
        # print ("passou por S3")
        self.rodar()

        time.sleep(3 * t)

        self.estatusS1 = False
        self.rodar()

        time.sleep(t)

        self.estatusS2 = False
        self.rodar()

        time.sleep(t)

        self.estatusS3 = False
        self.rodar()

    # ____________________Teste_______________________________________

    def TestCompleto(self):
        sim.simxFinish(-1)  # just in case, close all opened connections
        clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to CoppeliaSim
        if clientID != -1:
            print('Connected to remote API server')
            sim.simxAddStatusbarMessage(clientID, 'conectado a API...', sim.simx_opmode_oneshot)
            erro, Camera = sim.simxGetObjectHandle(clientID, 'Camera', sim.simx_opmode_oneshot_wait)
            erro, Bt = sim.simxGetObjectHandle(clientID, 'bt', sim.simx_opmode_oneshot_wait)

            TarefasTest.setInicio(clientID, Camera, Bt)
            print('Semaforo esta Verde')
            carros = 0
            time.sleep(1)
            tempoinicio = time.time()
            while carros < 500:
                tempoVerifica = time.time()
                self.semaforo = MonitorTimes.lerSemaforo()

                t = random.uniform(0.002, 0.1)
                print(t)
                td = random.uniform(0.5, 1)
                if (t < 0.008):
                    print("Nemum carro")
                else:
                    i = random.choice([1, 1, 2, 3, 4, 1, 5, 6, 1, 7, 1])
                    if i == 1:
                        self.todosOK(t)
                        time.sleep(td)
                    if i == 2:
                        self.perdeS1(t)
                        time.sleep(td)
                    if i == 3:
                        self.perdeS2(t)
                        time.sleep(td)
                    if i == 4:
                        self.perdeS3(t)
                        time.sleep(td)
                    if i == 5:
                        self.perdeS1eS2(t)
                        time.sleep(td)
                    if i == 6:
                        self.perdeS1eS3(t)
                        time.sleep(td)
                    if i == 7:
                        self.perdeS2eS3(t)
                        time.sleep(td)
                carros = carros + 1
                if abs(tempoVerifica - tempoinicio) > 20:
                    tempoinicio = tempoVerifica
                    print("verifica")
                    TarefasTest.verificaBt(sem=self.semaforo, tempos=self.temposVerificaBt).start()

        else:
            print('flaha ao conectar')


T = Teste()
T.TestCompleto()


temposS1 = pd.DataFrame({"tempos": T.temposS1})
temposS2 = pd.DataFrame({"tempos": T.temposS2})
temposS3 = pd.DataFrame({"tempos": T.temposS3})
temposCalculo = pd.DataFrame({"tempos": T.temposCalculo})
temposAtivarCamera = pd.DataFrame({"tempos": T.temposCamera})
temposMostrar = pd.DataFrame({"tempos": T.temposMostra})
temposVerificaBt = pd.DataFrame({"tempos": T.temposVerificaBt})
temposFalha = pd.DataFrame({"tempos": T.temposFalha})

graficoS1 = px.histogram(temposS1, x="tempos", title="Tempos de Execucao de Sensor1Ativado")
graficoS1.show()

graficoS2 = px.histogram(temposS2, x="tempos", title="Tempos de Execucao de Sensor2Ativado")
graficoS2.show()

graficoS3 = px.histogram(temposS3, x="tempos", title="Tempos de Execucao de Sensor3Ativado")
graficoS3.show()

graficoCalculo = px.histogram(temposCalculo, x="tempos", title="Tempos de Execucao de Calculo")
graficoCalculo.show()

graficoAtivarCamera = px.histogram(temposAtivarCamera, x="tempos", title="Tempos de Execucao de AtivaCamera")
graficoAtivarCamera.show()

graficoMostrar = px.histogram(temposMostrar, x="tempos", title="Tempos de Execucao de Mostrar")
graficoMostrar.show()

graficoVerificaBt = px.histogram(temposVerificaBt, x="tempos", title="Tempos de Execucao de VerificaBt")
graficoVerificaBt.show()

graficoFalha = px.histogram(temposFalha, x="tempos", title="Tempos de Execucao de Falha")
graficoFalha.show()
