import cv2
import copy
import os
from tqdm import tqdm

img = cv2.imread("sample.jpg")

def beep(freq, dur):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))

# 拡大（中心を支点にする）

def enlarge(img):
    enlargement = copy.deepcopy(img)

    a = len(img)
    b = len(img[0])
    c = len(img[0][0])
    bar = tqdm(total=a * b * c)
    temp = img[772:2316, 579:1737]

    A = len(temp)
    B = len(temp[0])
    C = len(temp[0][0])
    for i in range(A):
        for j in range(B):
            for k in range(C):
                enlargement[i * 2][j * 2][k] = temp[i][j][k]
                enlargement[i * 2 + 1][j * 2][k] = temp[i][j][k]
                enlargement[i * 2][j * 2 + 1][k] = temp[i][j][k]
                enlargement[i * 2 + 1][j * 2 + 1][k] = temp[i][j][k]
            bar.update(c * 4)

    beep(1000, 1000)
    return enlargement

enlargement = enlarge(img)
cv2.imwrite("enlarge.jpg", enlargement)