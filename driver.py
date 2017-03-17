#!/usr/bin/python

from NeuroPy import NeuroPy
#from classifier import Classifier
import Tkinter
#import gui class here
import time, sys

def startGUI():
    root = Tkinter.Tk()
    root.__init__
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    calib_canvas = Tkinter.Canvas(root, bg='white', height=screen_height, width=screen_width)
    calib_canvas.pack()
    dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]
    for val in dir_list:
        render_arrow(val, screen_width, screen_height, calib_canvas)
        root.update_idletasks()
        time.sleep(2)
        calib_canvas.delete('all')
        root.update_idletasks()


    root.mainloop()

def render_arrow(val, screen_width, screen_height, calib_canvas):
    w = screen_width
    h = screen_height
    upArrow = [w//2+h//12, h//2+w//8, w//2-h//12, h//2+w//8, w//2-h//12, h//2, w//2-h//6, h//2, w//2, h//2-w//8, w//2+h//6, h//2, w//2+h//12, h//2]
    rightArrow = [3*w//8, 7*h//12, 3*w//8, 5*h//12, w//2, 5*h//12, w//2, 4*h//12, 5*w//8, h//2, w//2, 8*h//12, w//2, 7*h//12]
    downArrow = [w//2-h//12, h//2-w//8, w//2+h//12, h//2-w//8, w//2+h//12, h//2, w//2+h//6, h//2, w//2, h//2+w//8, w//2-h//6, h//2, w//2-h//12, h//2]
    leftArrow = [5*w//8, 7*h//12, 5*w//8, 5*h//12, w//2, 5*h//12, w//2, 4*h//12, 3*w//8, h//2, w//2, 8*h//12, w//2, 7*h//12]

    if (val == 0):
        #render 'up' arrow
        calib_canvas.create_polygon(upArrow, outline='black', fill='black')
    elif (val == 1):
        #render 'right' arrow
        calib_canvas.create_polygon(rightArrow, outline='black', fill='black')
    elif (val == 2):
        calib_canvas.create_polygon(downArrow, outline='black', fill='black')
    else:
        #render 'left' arrow
        calib_canvas.create_polygon(leftArrow, outline='black', fill='black')
    calib_canvas.pack()


def main(argv):
    #start mindWave
    #c = Classifier()
    #start gui with instance of Classifier
    startGUI()
    #close gui after training data is added
    #train our classifier

    #c.train()
    # run function from driver that send key commands to the system





if __name__ == "__main__":
   main(sys.argv[1:])
