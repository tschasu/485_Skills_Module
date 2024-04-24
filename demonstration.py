from tkinter import *
import random
import time
mainWindow = Tk()

class ColorChanger:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Change Color", command=self.changeColor)
        self.button.pack()
        self.canvas = Canvas(window)
        self.canvas.pack()

    def changeColor(self):
        (centerX, centerY) = (int(self.canvas['width']) / 2, int(self.canvas['height']) / 2)
        radius = 100
        self.canvas.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius)

        while (True):
            self.window.configure(background=self.generateRandomColor())
            self.window.update()
            time.sleep(0.5)

    def obtainCurrentColor(self):
        return self.window["background"]
    
    def generateRandomColor(self):
        return "#" + random.randrange(0, 0x1000000).to_bytes(3, 'big').hex()

    

mainWindow.title('Demonstration')

ColorChanger(mainWindow)

quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

mainWindow.mainloop()