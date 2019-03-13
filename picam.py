from picamera import PiCamera
from time import sleep
 
camera = PiCamera()
 
# Запускаем предпросмотр сигнала с камеры на экране поверх всех окон
camera.start_preview()
 
# 10 секунд смотрим на экран
sleep(10)
 
# Выключаем предпросмотр
camera.stop_preview()