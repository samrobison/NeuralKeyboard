from Tkinter import *
from NeuroPy import NeuroPy
from time import *


class DataPack:
    val = -1
    data = []

class NK_Interface(Frame):

    def __init__(self, parent):

        global dataList
        dataList = []
        
        scale = 4
        Frame.__init__(self, parent, background='white')

        self.parent = parent

        pad = 0
        global screen_width
        screen_width = parent.winfo_screenwidth()
        global screen_height
        screen_height = parent.winfo_screenheight()
        self._geom = "{0}x{1}+0+0".format(screen_width, screen_height)
        parent.geometry("{0}x{1}+{2}+{3}".format(screen_width//scale, screen_height//scale, screen_width//2 - screen_width//(2*scale), screen_height//2 - screen_height//(2*scale)))

        parent.bind("<Escape>", self.toggle_full_manual)

    def initUI(self):

        #initialize global variables

        global setup_frame
        setup_frame = Frame(self, background='white')
        setup_frame.pack()
    
        #Main Window
        self.parent.title("Neural Keyboard")
        self.pack(fill=BOTH, expand=1)

        #Radio Buttons
        global radioVar
        radioVar = IntVar()
        radioVar = -1
        rbTextList = [("Arrows (B/W)    "),
                      ("Arrows (Color)  "),
                      ("Audio Cues      ")]
        radioButtonList = []
        for i in range(0, 3):
            radioButtonList.append(Radiobutton(setup_frame, text=rbTextList[i], variable=radioVar, value=i, background='white'))
            radioButtonList[i].grid(row=i)

        #Start Button
        startButton = Button(setup_frame, text="Begin Calibration")
        startButton.bind('<Button-1>', self.init_calib)
        startButton.grid(row=3)

        #Initialize Calibration Frame and Canvas (do not pack)
        global calib_frame
        calib_frame = Frame(self, background='white', width=screen_width, height=screen_height)

        global calib_canvas
        calib_canvas = Canvas(self, background='white', width=screen_width, height=screen_height)
        

    def toggle_full(self, event):
        geom = self.parent.winfo_geometry()
        self.parent.geometry(self._geom)
        self._geom = geom

    def toggle_full_manual(self, event):
        geom = self.parent.winfo_geometry()
        self.parent.geometry(self._geom)
        self._geom = geom

    def init_calib(self, event):
        setup_frame.pack_forget()
        self.toggle_full(event)
        calib_canvas.pack()
        calib_frame.pack()

        #list of calibration directions - 0 is up, 1 is right, 2 is down,  3 is left
        dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]

        for val in dir_list:

            data = []
            attention = []
            meditation = []
            rawValue = []
            delta = []
            theta = []
            lowAlpha = []
            highAlpha = []
            lowBeta = []
            highBeta = []
            lowGamma = []
            midGamma = []
            
            self.render_arrow(val)

            self.parent.update_idletasks()
            
            for i in range(0, 1000):
                #Append MindWave outputs:
                attention.append(i)
                meditation.append(i+1)
                rawValue.append(i+2)
                delta.append(i+3)
                theta.append(i+4)
                lowAlpha.append(i+5)
                highAlpha.append(i+6)
                lowBeta.append(i+7)
                highBeta.append(i+8)
                lowGamma.append(i+9)
                midGamma.append(i+10)
                sleep(0.001)
                
            data.append(attention)
            data.append(meditation)
            data.append(rawValue)
            data.append(delta)
            data.append(theta)
            data.append(lowAlpha)
            data.append(highAlpha)
            data.append(lowBeta)
            data.append(highBeta)
            data.append(lowGamma)
            data.append(midGamma)

            dataPack = DataPack()
            dataPack.val = val
            dataPack.data = data

            dataList.append(dataPack)

            calib_canvas.delete('all')
            self.parent.update_idletasks()
            sleep(1)

        self.parent.quit()

    def render_arrow(self, val):
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
            #render 'down' arrow
            calib_canvas.create_polygon(downArrow, outline='black', fill='black')
        else:
            #render 'left' arrow
            calib_canvas.create_polygon(leftArrow, outline='black', fill='black')
        calib_canvas.pack()
    
    def return_data(self):
        return dataList


def main():

    #set up classifier

    root = Tk()

    nk_inter = NK_Interface(root)

    nk_inter.initUI()
    
    root.mainloop()
    
    print("Calibration Complete.")

    dataList = nk_inter.return_data()

    for dataPack in dataList:
        print("val = ", dataPack.val)
        for array in dataPack.data:
            print array[0]

    root.destroy()

    #add data to classifier, continue with program.

if __name__ == '__main__':
    main()
