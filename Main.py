import pyautogui as pag
import keyboard
from winsound import Beep
while True:
    if keyboard.is_pressed('F3'): #F3을 클릭하면 매크로 실행
        Beep(524,200)
        Beep(587,200)
        Beep(659,200)
        Beep(698,200)
        Beep(784,200)
        break
while True:
    pag.click() 
    if keyboard.is_pressed('F4'): #F4를 클릭하면 매크로 종료
        Beep(784,200)
        Beep(698,200)
        Beep(659,200)
        Beep(587,200)
        Beep(524,200)
        break 
