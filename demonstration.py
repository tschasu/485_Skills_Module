from tkinter import *
mainWindow = Tk()

def changeColor():
    print("Does Not Do Anything Yet")

mainWindow.title('Demonstration')

button = Button(mainWindow, text="Change Color", command=changeColor)
button.pack()

quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

mainWindow.mainloop()