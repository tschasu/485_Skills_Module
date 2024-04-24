from tkinter import *
mainWindow = Tk()

class ColorChanger:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Change Color", command=self.changeColor)
        self.button.pack()

    def changeColor(mainWindow):
        print("Does not do anything yet")
    

mainWindow.title('Demonstration')

ColorChanger(mainWindow)

quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

mainWindow.mainloop()