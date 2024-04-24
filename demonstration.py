from tkinter import *
import random
import time
mainWindow = Tk()

class ColorChanger:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Change Color", command=self.changeColor)
        self.button.pack()

    def changeColor(self):
        self.window.configure(background=self.generateRandomColor())

    def obtainCurrentColor(self):
        return self.window["background"]
    
    def generateRandomColor(self):
        return "#" + random.randrange(0, 0x1000000).to_bytes(3, 'big').hex()

    

mainWindow.title('Demonstration')

ColorChanger(mainWindow)

quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

mainWindow.mainloop()