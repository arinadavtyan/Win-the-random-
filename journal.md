# Журнал проекта 

А тут описаны мои шаги по проекту. С Богом!


## Начнем с камеры!
вот такой вот кодик получился для запуска камеры и открывающегося окошка, чтобы игрок показывал свои пальцы 
```
import cv2  
import numpy as np  
# Обычно камера имеет номер 0  
cap = cv2.VideoCapture(0)  
while(cap.isOpened()):  
   # Читаем очередной кадр  
  ret, frame = cap.read()  
   # Задерживаем на 1 миллисекунду, ждем нажатия q  
  if cv2.waitKey(1) & 0xFF == ord('q') or not ret:  
        break  
  # Переводим изображение в монохром  
 # И отображаем кадры в одном и том же окне  cv2.imshow('Победи рандом', frame)  
   cv2.waitKey(1)  
cv2.destroyAllWindows()
```

![unchanged image](cap.png)


## Дальше генерируем число 
```
k=(random.randint(0, 4))
```
вы спросите почему 4?
Потому что:
## Сложность номер 1
я поняла что мне придется показывать от 0-4 пальцев, потому что прописать индекс большого пальца невозможно. И при поднятом состоянии и при прижатом там все одинаково. 

## Тут я читаю индексы ручки 
```
if results.multi_hand_landmarks is not None:  
   # нас интересует только подушечка указательного пальца (индекс 8)  
 # нужно умножить координаты а размеры картинки  y_6 = int(results.multi_hand_landmarks[0].landmark[6].y *  
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
              flippedRGB.shape[0]
```
Все работает, я очень рада!
Теперь я немного поменяю beggining и закомичю новую версию, потому что в старой я просто не учла хэнд детектор. 

## 





