###############
from PIL import ImageGrab
from PIL import Image
import pynput
import time
import os
import keyboard
###############

#Define Vars
mouse = pynput.mouse.Controller()
Latch = False
MousePosLatch = True
#Finding Mouse Pos
time.sleep(5)
X, Y = pynput.mouse.Controller().position
ScreenShot = ImageGrab.grab()
ScreenShot.save("Screenshot.png")
#Find Pixel Color at mouse pos
im = Image.open("Screenshot.png")
rgb_im = im.convert("RGB")
R, G, B = rgb_im.getpixel((X, Y))

os.remove("Screenshot.png")
time.sleep(3)
mouse.position = (840, 979)


while True:
    #Capturing Screen
    ScreenShot = ImageGrab.grab()
    ScreenShot.save("Screenshot.png")
    #Finding pixel color
    im = Image.open('Screenshot.png')
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((970, Y))

    print(r, g, b)
    #Checking if pixel color is equal to set pixel color
    if r == R and g == G and b == B and Latch == True:
        #Setting the Block latch
        Latch == False
        
        if MousePosLatch == True:
            MousePosLatch = False
            mouse.position = (960, 980)
            mouse.click(pynput.mouse.Button.left)
        elif MousePosLatch == False:
            MousePosLatch = True
            mouse.position = (840, 979)
            mouse.click(pynput.mouse.Button.left)
    elif r == 255 and g == 255 and b == 255 and Latch == False:
        Latch = True

    os.remove("Screenshot.png")
    if keyboard.is_pressed('l'):
            break