import tkinter
mainWindow = tkinter.Tk()

mainWindow.title('Demonstration')
button = tkinter.Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
button.pack()
mainWindow.mainloop()

print("TODO: DEMONSTRATE")