from NeuroPy import NeuroPy
from time import *
from PIL import Image, ImageTk
import tkFont
import pyaudio
import wave
import Tkinter as tk


class NK_Interface:

    def __init__(self, color, audio, delay):
        self.dataList = []
        self.color = color
        self.audio = audio
        self.delay = delay
        self.currentData = False
        if audio == 1:
            self.p = pyaudio.PyAudio()

    def callBackFunc(self, val):
        if self.currentData != False:
            self.currentData.append(val)

    def init_calib(self):
        self.parent = tk.Tk()
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.numfont = tkFont.Font(family='Helvetica', size=144, weight='bold')
        self.textFont = tkFont.Font(family='Helvetica', size=72, weight='bold')
        self.calib_canvas = tk.Canvas(self.parent, width=self.screen_width, height=self.screen_height)
        self.calib_canvas.pack()

        #set up arrows to store in ram
        if(self.color == 0):
            self.left = ImageTk.PhotoImage(Image.open("resources/images/leftarrow.png"))
            self.right = ImageTk.PhotoImage(Image.open("resources/images/rightarrow.png"))
            self.up = ImageTk.PhotoImage(Image.open("resources/images/uparrow.png"))
            self.down = ImageTk.PhotoImage(Image.open("resources/images/downarrow.png"))

        else:
            self.left = ImageTk.PhotoImage(Image.open("resources/images/leftarrowblue.png"))
            self.right = ImageTk.PhotoImage(Image.open("resources/images/rightarrowred.png"))
            self.up = ImageTk.PhotoImage(Image.open("resources/images/uparrowyellow.png"))
            self.down = ImageTk.PhotoImage(Image.open("resources/images/downarrowgreen.png"))

        #start MindWave
        mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)
        mindWave.start()

        #start call back
        mindWave.setCallBack("rawValue", self.callBackFunc)

        #initiate calibration countdown:
        self.calib_canvas.delete("all")
        sleep(5)
        self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="5", font=self.numfont)
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        self.calib_canvas.delete("all")
        self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="4", font=self.numfont)
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        self.calib_canvas.delete("all")
        self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="3", font=self.numfont)
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        self.calib_canvas.delete("all")
        self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="2", font=self.numfont)
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        self.calib_canvas.delete("all")
        self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="1", font=self.numfont)
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)
        self.calib_canvas.delete("all")
        self.calib_canvas.pack()
        self.parent.update_idletasks()
        sleep(1)


        #list of calibration directions - 0 is up, 1 is right, 2 is down,  3 is left
        dir_list = [0,1,2,3,2,1,3,0,2,1,0,3,0,3,2,1,3,2,0,1]
        #dir_list = [0,1,2,]
        skip = True
        for val in dir_list:

            label = self.render_arrow(val,skip)
            skip = False

            #let the callback collect data
            self.currentData = []

            sleep(3)

            self.calib_canvas.delete('all')
            self.parent.update_idletasks()

            #stop collection
            trial = self.currentData[:]
            self.currentData = False
            #add data with label to data list
            self.dataList.append([trial, label])

            sleep(self.delay)
        self.calib_canvas.delete("all")
        #self.calib_canvas.create_text(self.screen_width//2, self.screen_height//2, text="Press Escape to Finish Calibration", font=self.textFont)
        self.parent.destroy()

    def render_arrow(self, val,skip):

        if (val == 0):
            label = "up"
            #render 'up' arrow
            self.calib_canvas.create_image(self.screen_width/2, self.screen_height/2, image=self.up)
            self.calib_canvas.pack()
            self.parent.update_idletasks()
            if skip:
                return
            #calib_canvas.create_image(w//2 - upArrow.width()//2, h//2 - upArrow.height()//2, image=upArrow)
            if(self.audio == 1):
                f = wave.open("./resources/audio/Audio_U.wav", "rb")
                #play audio
                stream = self.p.open(format=self.p.get_format_from_width(f.getsampwidth()),
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
            label =  "right"
            #render 'right' arrow
            self.calib_canvas.create_image(self.screen_width/2, self.screen_height/2, image=self.right)
            self.calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - rightArrow.width()//2, h//2 - rightArrow.height()//2, image=rightArrow)
            if(self.audio == 1):
                f = wave.open("./resources/audio/Audio_R.wav", "rb")
                #play audio
                stream = self.p.open(format=self.p.get_format_from_width(f.getsampwidth()),
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
            label = "down"
            #render 'down' arrow
            self.calib_canvas.create_image(self.screen_width/2, self.screen_height/2, image=self.down)
            self.calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - downArrow.width()//2, h//2 - downArrow.height()//2, image=downArrow)
            if(self.audio == 1):
                f = wave.open("./resources/audio/Audio_D.wav", "rb")
                #play audio
                stream = self.p.open(format=self.p.get_format_from_width(f.getsampwidth()),
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
            label =  "left"
            #render 'left' arrow
            self.calib_canvas.create_image(self.screen_width/2, self.screen_height/2, image=self.left)
            self.calib_canvas.pack()
            self.parent.update_idletasks()
            #calib_canvas.create_image(w//2 - leftArrow.width()//2, h//2 - leftArrow.height()//2, image=leftArrow)
            if(self.audio == 1):
                f = wave.open("./resources/audio/Audio_L.wav", "rb")
                #play audio
                stream = self.p.open(format=self.p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output=True)
                data = f.readframes(1024)
                while data:
                    stream.write(data)
                    data = f.readframes(1024)
                stream.stop_stream()
                stream.close()
            return label

    def exit_loop(self, event):
        self.parent.quit()

    def return_data(self):
        return self.dataList

# def main():
#
#     #set up classifier
#     global color
#     color = int(sys.argv[1])
#     global audio
#     audio = int(sys.argv[2])
#     global delay
#     delay = int(sys.argv[3])
#
#     root = Tk()
#
#     global numFont
#     numFont = tkFont.Font(family='Helvetica', size=144, weight='bold')
#     global textFont
#     textFont = tkFont.Font(family='Helvetica', size=72, weight='bold')
#
#     global p
#     p = pyaudio.PyAudio()
#
#     nk_inter = NK_Interface(root)
#
#     root.mainloop()
#
#     print("Calibration Complete.")
#
#     self.datalist = nk_inter.return_data()
#
#     for dataPack in self.datalist:
#         print("val = ", dataPack.val)
#         for array in dataPack.data:
#             print array[0]
#
#     root.destroy()
#
#     #add data to classifier, continue with program.
#
# if __name__ == '__main__':
#     main()
