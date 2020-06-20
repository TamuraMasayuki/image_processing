import cv2
import copy
import os
from tqdm import tqdm

img = cv2.imread("sample.jpg")

def beep(freq, dur):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))

# ミラー
def mirror(img):
    img_mirror = copy.deepcopy(img)
    a = len(img)
    b = len(img[0])
    c = len(img[0][0])
    bar = tqdm(total = a * b / 2)
    for i in range(a):
        for j in range(int(b/2)):
            img_mirror[i][j] = img[i][b-j-1]
            bar.update(1)

    beep(500, 1000)
    return img_mirror

img_mirror = mirror(img)
cv2.imwrite("mirror.jpg", img_mirror)