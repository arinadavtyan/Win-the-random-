import cv2
import numpy as np
cap = cv2.VideoCapture(0)
name_of_player1 = input()
name_of_player2 = input()
while(cap.isOpened()):
   # Читаем очередной кадр
   ret, frame = cap.read()
   cv2.imshow(name_of_player1, ret)
   cv2.imshow(name_of_player2, frame)
   # Задерживаем на 1 миллисекунду, ждем нажатия q
   if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
cv2.destroyAllWindows()
import cv2
# Обычно камера имеет номер 0
cap = cv2.VideoCapture(0)
# В цикле, пока есть соединение с камерой
# (например, USB-камеру можно отсоединить в процессе
