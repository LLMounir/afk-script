"""
script pour afk;
bouge la souris de 1 vers la droite toute les 10 secondes
"""
from pynput.mouse import Button, Controller
import time
import random

time.sleep(10)
mouse = Controller()
i = 0
while i< 300:
  i += 1
  print("Mouse clicked")
  time.sleep(1)
  mouse.press(Button.left)
  mouse.release(Button.left)
