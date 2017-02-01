from NeuroPy import NeuroPy
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)

fig, ax = plt.subplots()
mindWave.start()

x = np.arange(0, 100, 1)
z = np.arange(0, 100, 1)
line, = ax.plot(x, x, label="Attention",c='r' )
line2, = ax.plot(x, x,label="Meditation",c='b' )
def animate(i):
    global x, z
    attention = mindWave.attention
    meditation = mindWave.meditation

    tmpList = x.tolist()
    tmpList.append(attention)
    tmpList.remove(tmpList[0])
    x = np.array(tmpList)

    line.set_ydata(x)

    tmpList = z.tolist()
    tmpList.append(meditation)
    tmpList.remove(tmpList[0])
    z = np.array(tmpList)

    line2.set_ydata(z)

    print "Attention: "+str(attention)+" Meditation: "+str(meditation)
    #line2 = mindWave.meditation
    return [line, line2]

def init():
    line.set_ydata(mindWave.attention)
    return line

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init)
plt.legend(loc="upper left")
plt.show()
