import os
import win32com.client
import pyautogui
import cv2
import time
import random
import numpy as np

#pip3 install numpy
#pip3 install opencv-python
#pip3 install pyautogui


allfish = 0
primanka = 0

# Автоматически установите рабочий стол пользователя в качестве пути к файлу
os.chdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

# Создать экземпляр для отправки нажатия клавиш в Windows
shell = win32com.client.Dispatch("WScript.Shell")

def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

# Количество забросов. Дефолт 150. дальше идет авто кик за бездействие +-30 забросов
number_of_fishing_rods = 150
print(" ")
print("Maden: 0ri0n | Бот Рыбака.")
print("Расход: 30 минут - 80-100 удочек")
print("Версия: 0.1")
print(" ")

caught_fish_counter = 0
timeout_start_fishing = time.time()
for i in range(int(number_of_fishing_rods)):
    timeout = 34
    timeout_start = time.time()
    pos_fish=[-1,-1]
    while (pos_fish[0]==-1) and (time.time()<(timeout_start+timeout)):
        pos_fish=imagesearch("C:/fish/2.png")

    shell.SendKeys("w")
    allfish += 1

    if (time.time()-timeout_start)<timeout and i<(int(number_of_fishing_rods)-1):
        time.sleep(6)
        time.sleep(random.randint(5,10)/10)
        primanka += 1
        if primanka >= 4:
            primanka = 0
            shell.SendKeys("s")
            time.sleep(4)
        shell.SendKeys("w")
        caught_fish_counter += 1
        print("Всего (All Fish): ", allfish)

print(" ")
print("Вы поймали: {} Рыб с {} попыток. Шанс успеха {}%.".format(int(caught_fish_counter),int(number_of_fishing_rods),round(int(caught_fish_counter)/int(number_of_fishing_rods)*100)))
print("Потрачено времени: {} минут.".format(round((time.time()-timeout_start_fishing)/60)))
time.sleep(60)
