from Tkinter import *
from NeuroPy import NeuroPy
from time import *
import tkFont
import pyaudio
import wave

class DataPack:
    val = -1
    data = []

class NK_Interface(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)

        global dataList
        dataList = []
        
        scale = 4
        Frame.__init__(self, parent, background='white')

        self.parent = parent

        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        parent.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
    
        #Main Window
        self.parent.title("Neural Keyboard")
        self.pack(fill=BOTH, expand=1)

        #Initialize Calibration Canvas (do not pack)

        calib_canvas = Canvas(self, background='white', width=screen_width, height=screen_height)

        #self.init_calib()
        parent.bind("<Escape>", self.exit_loop)
        self.init_calib(screen_width, screen_height, calib_canvas)
        
    def init_calib(self, screen_width, screen_height, calib_canvas):
        calib_canvas.pack()

        #upArrow = PhotoImage("resources/images/Arrow_U.ppm")
        #rightArrow = PhotoImage("resources/images/Arrow_R.ppm")
        #downArrow = PhotoImage("resources/images/Arrow_D.ppm")
        #leftArrow = PhotoImage("resources/images/Arrow_L.ppm")

        #initiate calibration countdown:
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="5", font=numFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="4", font=numFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="3", font=numFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="2", font=numFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="1", font=numFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        calib_canvas.delete("all")
        calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        
        
        #list of calibration directions - 0 is up, 1 is right, 2 is down,  3 is left
        dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]

        for val in dir_list:

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
            
            self.render_arrow(val, screen_width, screen_height, calib_canvas)
            
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
            self.parent.update_idletasks()
            sleep(delay)
        calib_canvas.delete("all")
        calib_canvas.create_text(screen_width//2, screen_height//2, text="Press Escape to Finish Calibration", font=textFont)
        calib_canvas.pack()
        self.parent.update_idletasks()
        
        p.terminate()

    def render_arrow(self, val, screen_width, screen_height, calib_canvas):
        
        w = screen_width
        h = screen_height

        upArrow = [w//2+h//12, h//2+w//8, w//2-h//12, h//2+w//8, w//2-h//12, h//2, w//2-h//6, h//2, w//2, h//2-w//8, w//2+h//6, h//2, w//2+h//12, h//2]
        rightArrow = [3*w//8, 7*h//12, 3*w//8, 5*h//12, w//2, 5*h//12, w//2, 4*h//12, 5*w//8, h//2, w//2, 8*h//12, w//2, 7*h//12]
        downArrow = [w//2-h//12, h//2-w//8, w//2+h//12, h//2-w//8, w//2+h//12, h//2, w//2+h//6, h//2, w//2, h//2+w//8, w//2-h//6, h//2, w//2-h//12, h//2]
        leftArrow = [5*w//8, 7*h//12, 5*w//8, 5*h//12, w//2, 5*h//12, w//2, 4*h//12, 3*w//8, h//2, w//2, 8*h//12, w//2, 7*h//12]


        if(color == 0):
            color_u = 'black'
            color_r = 'black'
            color_d = 'black'
            color_l = 'black'
        
        else:
            color_u = 'yellow'
            color_r = 'red'
            color_d = 'green'
            color_l = 'blue'
        
        if (val == 0):
            #render 'up' arrow
            calib_canvas.create_polygon(upArrow, fill=color_u, outline=color_u)
            calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - upArrow.width()//2, h//2 - upArrow.height()//2, image=upArrow)
            if(audio == 1):
                f = wave.open("./resources/audio/Audio_U.wav", "rb")
                #play audio
                stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output=True)
                data = f.readframes(1024)
                while data:
                    stream.write(data)
                    data = f.readframes(1024)
                stream.stop_stream()
                stream.close()
        elif (val == 1):
            #render 'right' arrow
            calib_canvas.create_polygon(rightArrow, fill=color_r, outline=color_r)
            calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - rightArrow.width()//2, h//2 - rightArrow.height()//2, image=rightArrow)
            if(audio == 1):
                f = wave.open("./resources/audio/Audio_R.wav", "rb")
                #play audio
                stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output=True)
                data = f.readframes(1024)
                while data:
                    stream.write(data)
                    data = f.readframes(1024)
                stream.stop_stream()
                stream.close()
        elif (val == 2):
            #render 'down' arrow
            calib_canvas.create_polygon(downArrow, fill=color_d, outline=color_d)
            calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - downArrow.width()//2, h//2 - downArrow.height()//2, image=downArrow)
            if(audio == 1):
                f = wave.open("./resources/audio/Audio_D.wav", "rb")
                #play audio
                stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output=True)
                data = f.readframes(1024)
                while data:
                    stream.write(data)
                    data = f.readframes(1024)
                stream.stop_stream()
                stream.close()
        else:
            #render 'left' arrow
            calib_canvas.create_polygon(leftArrow, fill=color_l, outline=color_l)
            calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - leftArrow.width()//2, h//2 - leftArrow.height()//2, image=leftArrow)
            if(audio == 1):
                f = wave.open("./resources/audio/Audio_L.wav", "rb")
                #play audio
                stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output=True)
                data = f.readframes(1024)
                while data:
                    stream.write(data)
                    data = f.readframes(1024)
                stream.stop_stream()
                stream.close()
            
    def exit_loop(self, event):
        self.parent.quit()
    
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

    global numFont
    numFont = tkFont.Font(family='Helvetica', size=144, weight='bold')
    global textFont
    textFont = tkFont.Font(family='Helvetica', size=72, weight='bold')

    global p
    p = pyaudio.PyAudio()

    nk_inter = NK_Interface(root)
    
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
