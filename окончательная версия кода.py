import time

import cv2
import numpy as np
import mediapipe as mp
import random

#переменные с цветами
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

selected_random = None
from_selection = None
CONFIRMATION_TIME = 3
computers_number = random.randint(1, 4)

game_end = False

'''функция принимает три аргумента: картинку на которой текст, сам текст, цвет текста '''
def center_text(image, text, color):
    font = cv2.FONT_HERSHEY_SIMPLEX

    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    textX = round((image.shape[1] - textsize[0]) / 2)
    textY = round((image.shape[0] + textsize[1]) / 2)
    cv2.putText(image, text, (textX, textY), font, 1, color, 2)


fingers = 0
k = 0
# Обычно камера имеет номер 0
cap = cv2.VideoCapture(0)
handsDetector = mp.solutions.hands.Hands()
# В цикле, пока есть соединение с камерой
# (например, USB-камеру можно отсоединить в процессе
while (cap.isOpened()):
    # Читаем очередной кадр
    ret, frame = cap.read()
    # Задерживаем на 1 миллисекунду, ждем нажатия q
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    # Переводим изображение в монохром
    flippedRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Распознаем
    results = handsDetector.process(flippedRGB)
    # ОПРЕДЕЛЯЕМ ИНДЕКСЫ ПАЛЬЦЕВ ОДНОЙ РУКИ

    fingers = None
    if results.multi_hand_landmarks is not None:
        y_6 = int(results.multi_hand_landmarks[0].landmark[6].y *
                  flippedRGB.shape[0])
        y_8 = int(results.multi_hand_landmarks[0].landmark[8].y *
                  flippedRGB.shape[0])
        y_10 = int(results.multi_hand_landmarks[0].landmark[10].y *
                   flippedRGB.shape[0])
        y_12 = int(results.multi_hand_landmarks[0].landmark[12].y *
                   flippedRGB.shape[0])
        y_14 = int(results.multi_hand_landmarks[0].landmark[14].y *
                   flippedRGB.shape[0])
        y_16 = int(results.multi_hand_landmarks[0].landmark[16].y *
                   flippedRGB.shape[0])
        y_18 = int(results.multi_hand_landmarks[0].landmark[19].y *
                   flippedRGB.shape[0])
        y_20 = int(results.multi_hand_landmarks[0].landmark[20].y *
                   flippedRGB.shape[0])
        if y_6 < y_8 and y_10 < y_12 and y_14 < y_16 and y_18 < y_20:
            fingers = 0
        if y_6 > y_8 and y_10 < y_12 and y_14 < y_16 and y_18 < y_20:
            fingers = 1
        if y_6 > y_8 and y_10 > y_12 and y_14 < y_16 and y_18 < y_20:
            fingers = 2
        if y_6 > y_8 and y_10 > y_12 and y_14 > y_16 and y_18 < y_20:
            fingers = 3
        if y_6 > y_8 and y_10 > y_12 and y_14 > y_16 and y_18 > y_20:
            fingers = 4

    if fingers or game_end:
        if fingers is not None and fingers != selected_random:
            selected_random = fingers
            from_selection = time.time()
            end_game = False
            computers_number = random.randint(1, 4)
        time_shown = time.time() - from_selection
        time_left = CONFIRMATION_TIME - time_shown

        if game_end or time_left < 0:
            if selected_random == computers_number:
                center_text(frame, f'Win!', GREEN)
            else:
                center_text(frame, f'Lose, the right number was {computers_number}', RED)
        else:
            center_text(frame, f'{round(time_left)}...', BLUE)
    else:
        selected_random = None
        center_text(frame, 'Show any number from 1 to 4', BLUE)
    cv2.imshow('Win the random', frame)
    cv2.waitKey(1)

# освобождаем ресурсы
handsDetector.close()
cv2.destroyAllWindows()