import cv2
import copy
import os
from tqdm import tqdm
import numpy as np

img = cv2.imread("sample.jpg")

def beep(freq, dur):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))

# 光のトンネル

def LightTunnel(img):
    light_tunnel = copy.deepcopy(img)

    a = len(img)
    b = len(img[0])

    bar = tqdm(total=a * b)

    o1 = 3087 / 2
    o2 = 2315 / 2

    for i in range(a):
        for j in range(b):
            l_2 = (i - o1)**2 + (j - o2)**2
            if l_2 > 514**2:
                I = int(514 / np.sqrt(l_2) * (i - o1) + o1)
                J = int(514 / np.sqrt(l_2) * (j - o2) + o2)
                light_tunnel[i][j] = img[I][J]
            bar.update(1)

    beep(500, 1000)
    return light_tunnel

light_tunnel = LightTunnel(img)
cv2.imwrite("light_tunnel.jpg", light_tunnel)