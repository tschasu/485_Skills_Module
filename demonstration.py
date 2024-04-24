from tkinter import *
import random
import time

# Color Changer Class
class ColorChanger:
    # Constructor
    def __init__(self, window):
        self.window = window
        
        # Pack the button with the change color method as the target
        self.button = Button(window, text="Acivate Disco Ball", command=self.changeColor)
        self.button.pack()

        # create and save the canvas, packing
        self.canvas = Canvas(window)
        self.canvas.pack()

    # Draws a disco ball and randomly changes its colors
    def changeColor(self):
        # Obtain the center of the canvas, set the radius of the disco ball
        (centerX, centerY) = (int(self.canvas['width']) / 2, int(self.canvas['height']) / 2)
        radius = 100

        # An error is thrown once the GUI is ended, this catches it
        try:
            # Loop infinitely
            while (True):
                # Clear canvas
                self.canvas.delete("all")

                # Draw base disco ball with color
                self.canvas.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, fill=self.generateRandomColor())

                # Draw outlines to enhance disco ball look
                for i in range(20, 120, 20):
                    self.canvas.create_oval(centerX - (radius - i), centerY - radius, centerX + (radius - i), centerY + radius)
                    self.canvas.create_oval(centerX - radius, centerY - (radius - i), centerX + radius, centerY + (radius - i))

                # Wait for the drawings to complete
                self.window.update()

                # Pause for half a second before looping again
                time.sleep(0.5)
        except:
            print("Complete")

    def obtainCurrentColor(self):
        return self.window["background"]
    
    def generateRandomColor(self):
        return "#" + random.randrange(0, 0x1000000).to_bytes(3, 'big').hex()

    
# Create the main window and its title
mainWindow = Tk()
mainWindow.title('Demonstration')

# Set up the disco functionality
ColorChanger(mainWindow)

# Provide a quit button, packing it
quitButton = Button(mainWindow, text='Quit Demonstration', command=mainWindow.destroy)
quitButton.pack()

# Begin the main window loop
mainWindow.mainloop()