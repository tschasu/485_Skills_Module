from tkinter import *
import random
import time
mainWindow = Tk()

class ColorChanger:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Acivate Disco Ball", command=self.changeColor)
        self.button.pack()
        self.canvas = Canvas(window)
        self.canvas.pack()

    def changeColor(self):
        (centerX, centerY) = (int(self.canvas['width']) / 2, int(self.canvas['height']) / 2)
        radius = 100

        try:
            while (True):
                # self.window.configure(background=self.generateRandomColor())
                self.canvas.delete("all")
                self.canvas.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, fill=self.generateRandomColor())
                for i in range(20, 120, 20):
                    self.canvas.create_oval(centerX - (radius - i), centerY - radius, centerX + (radius - i), centerY + radius)
                    self.canvas.create_oval(centerX - radius, centerY - (radius - i), centerX + radius, centerY + (radius - i))
                self.window.update()
                time.sleep(0.5)
        except:
            print("Complete")

    def obtainCurrentColor(self):
        return self.window["background"]
    
    def generateRandomColor(self):
        return "#" + random.randrange(0, 0x1000000).to_bytes(3, 'big').hex()

    

mainWindow.title('Demonstration')

ColorChanger(mainWindow)

quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

mainWindow.mainloop()