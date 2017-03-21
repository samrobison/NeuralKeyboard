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
        self._geom = "{0}x{1}+{2}+{3}".format(screen_width//scale, screen_height//scale, screen_width//2 - screen_width//(2*scale), screen_height//2 - screen_height//(2*scale))
        parent.geometry("{0}x{1}+0+0".format(screen_width, screen_height))

        parent.bind("<Escape>", self.toggle_full_manual)

    def initUI(self):
    
        #Main Window
        self.parent.title("Neural Keyboard")
        self.pack(fill=BOTH, expand=1)

        #Initialize Calibration Frame and Canvas (do not pack)
        global calib_frame
        calib_frame = Frame(self, background='white', width=screen_width, height=screen_height)

        global calib_canvas
        calib_canvas = Canvas(self, background='white', width=screen_width, height=screen_height)

        self.init_calib()
        

    def toggle_full(self):
        geom = self.parent.winfo_geometry()
        self.parent.geometry(self._geom)
        self._geom = geom

    def toggle_full_manual(self, event):
        geom = self.parent.winfo_geometry()
        self.parent.geometry(self._geom)
        self._geom = geom

    def init_calib(self):
        calib_canvas.pack()
        calib_frame.pack()

        #upArrow = PhotoImage("resources/images/Arrow_U.ppm")
        #rightArrow = PhotoImage("resources/images/Arrow_R.ppm")
        #downArrow = PhotoImage("resources/images/Arrow_D.ppm")
        #leftArrow = PhotoImage("resources/images/Arrow_L.ppm")
        
        #list of calibration directions - 0 is up, 1 is right, 2 is down,  3 is left
        dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]

        for val in dir_list:

##            if(val == 0):
##                calib_canvas = Label(self, image=upArrow)
##                calib_canvas.image = upArrow
##            elif(val == 1):
##                calib_canvas = Label(self, image=rightArrow)
##                calib_canvas.image = rightArrow
##            elif(val == 2):
##                calib_canvas = Label(self, image=downArrow)
##                calib_canvas.image = downArrow
##            else:
##                calib_canvas = Label(self, image=leftArrow)
##                calib_canvas.image = leftArrow

            data = []
            delta = []
            theta = []
            lowAlpha = []
            highAlpha = []
            lowBeta = []
            highBeta = []
            lowGamma = []
            midGamma = []
            
            w = screen_width
            h = screen_height
            
            #calib_canvas.create_image(w//2 - calib_canvas.image.width()//2, h//2 - calib_canvas.image.height()//2, image=calib_canvas.image)
            self.render_arrow(val)
            calib_canvas.pack()

            self.parent.update_idletasks()
            
            for i in range(0, delay * 1000):
                #Append MindWave outputs:
                delta.append(i)
                theta.append(i+1)
                lowAlpha.append(i+2)
                highAlpha.append(i+3)
                lowBeta.append(i+4)
                highBeta.append(i+5)
                lowGamma.append(i+6)
                midGamma.append(i+7)
                sleep(0.001)
                
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
            #calib_canvas.pack_forget()
            self.parent.update_idletasks()
            sleep(delay)

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
            calib_canvas.create_polygon(upArrow, fill='black', outline='black')
            #calib_canvas.create_image(w//2 - upArrow.width()//2, h//2 - upArrow.height()//2, image=upArrow)
        elif (val == 1):
            #render 'right' arrow
            calib_canvas.create_polygon(rightArrow, fill='black', outline='black')
            #calib_canvas.create_image(w//2 - rightArrow.width()//2, h//2 - rightArrow.height()//2, image=rightArrow)
        elif (val == 2):
            #render 'down' arrow
            calib_canvas.create_polygon(downArrow, fill='black', outline='black')
            #calib_canvas.create_image(w//2 - downArrow.width()//2, h//2 - downArrow.height()//2, image=downArrow)
        else:
            #render 'left' arrow
            calib_canvas.create_polygon(leftArrow, fill='black', outline='black')
            #calib_canvas.create_image(w//2 - leftArrow.width()//2, h//2 - leftArrow.height()//2, image=leftArrow)
    
    def return_data(self):
        return dataList


def main():

    #set up classifier
    global color
    color = int(sys.argv[1])
    global audio
    audio = int(sys.argv[2])
    global delay
    delay = int(sys.argv[3])

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
