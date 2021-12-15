import cv2
import numpy as np
# Обычно камера имеет номер 0
cap = cv2.VideoCapture(0)
# В цикле, пока есть соединение с камерой
# (например, USB-камеру можно отсоединить в процессе
while(cap.isOpened()):
   # Читаем очередной кадр
   ret, frame = cap.read()
   # Задерживаем на 1 миллисекунду, ждем нажатия q
   if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
   # Переводим изображение в монохром
   # И отображаем кадры в одном и том же окне
   cv2.imshow('Победи рандом', frame)
   cv2.waitKey(1)
cv2.destroyAllWindows()