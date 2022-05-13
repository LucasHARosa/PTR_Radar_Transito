import sim
import numpy as np
import matplotlib.pyplot as mlp
import time

def tirafoto(camera,clientID):
    time.sleep(0.3)
    erro,resolution,arrayimagem = sim.simxGetVisionSensorImage(clientID,camera,0,sim.simx_opmode_oneshot_wait)
    im = np.array(arrayimagem, dtype=np.uint8)
    im.resize([resolution[0], resolution[1], 3])
    mlp.imshow(im,origin='lower')
    mlp.show()
    