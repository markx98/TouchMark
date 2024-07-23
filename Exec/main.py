import pyautogui
import time
import requests
from tkinter import *


def touch():
    vizualizer = int()
    vizualizer in range(5, -1, -1)
    time.sleep(0.5)
    timescreen['text'] = f'''
    {vizualizer}'''

    mark = (pyautogui.position())
    response['text'] = f'''
    {mark}'''
    pyautogui.scroll(5000)

    

window = Tk()
window.title("Touch The Screen")
texto = Label(window, text="Click to Touch the Screen")
texto.grid(column=0, row=1, padx=50, pady=10)

timescreen = Label(window, text ='')
timescreen.grid(column=0, row=2, padx=50, pady=10)

botao = Button(window, text=" Touch ", command=touch,) 
botao.grid(column=0, row=3, padx=50, pady=10)

response = Label(window, text="SCREEN POSITION")
response.grid(column=0, row=4, padx=50, pady=10)


window.mainloop()