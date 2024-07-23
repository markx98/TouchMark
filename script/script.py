from tkinter import *
import pyautogui
import time

def touch():
    for vizualizer in range(5, -1, -1):
        print(vizualizer, end=' ')
        time.sleep(0.5)
        timescreen['text'] = vizualizer
        window.update()
        timescreen['text'] = 'READY'
    
    mark = (pyautogui.position())
    response['text'] = f''' {mark}'''
    pyautogui.scroll(5000) 


window = Tk()
window.geometry('265x215')
window.title("Touch Screen")


timescreen = Label(window, text ='')
timescreen.grid(column=0, row=2, padx=50, pady=10)

texto = Label(window, text="CLICK TO TOUCH THE SCREEN")
texto.grid(column=0, row=1, padx=50, pady=10)

botao = Button(window, text=" Touch ", command=touch) 
botao.grid(column=0, row=3, padx=50, pady=10)

response = Label(window, text="SCREEN POSITION")
response.grid(column=0, row=4, padx=50, pady=10) 


window.mainloop()