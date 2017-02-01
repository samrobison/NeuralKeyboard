from NeuroPy import NeuroPy
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def alphaBetaGamma():
    global mindWave, lines,halpha,lalpha, lbeta, hbeta, mgamma, lgamma
    mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)

    mindWave.start()
    fig, ax = plt.subplots()

    global mindWave
    lines = []
    for i in range(6):
        lines.append(np.arange(0, 50000, 200))

    halpha, = ax.plot(lines[0], lines[0], label="High Alpha",c='#02FFFF' )
    lalpha, = ax.plot(lines[0], lines[0],label="Low Alpha",c='#77BDF0' )
    hbeta, = ax.plot(lines[0], lines[0],label="High Beta",c='#02FF3B' )
    lbeta, = ax.plot(lines[0], lines[0],label="Low Beta",c='#06AB0D' )
    mgamma, = ax.plot(lines[0], lines[0],label="Mid Gamma",c='#FF0000' )
    lgamma, = ax.plot(lines[0], lines[0],label="Low Gamma",c='#BA2E2E' )

    ani = animation.FuncAnimation(fig, animateABG, np.arange(1, 200), init_func=init)
    plt.legend(loc="upper left")
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)

    plt.show()



def attentionMeditation():
    global mindWave, x,z,line,line2
    mindWave = NeuroPy("/dev/tty.MindWaveMobile-DevA", 57600)

    mindWave.start()
    fig, ax = plt.subplots()

    x = np.arange(0, 100, .3)
    z = np.arange(0, 100, .3)
    line, = ax.plot(x, x, label="Attention",c='r' )
    line2, = ax.plot(x, x,label="Meditation",c='b' )

    ani = animation.FuncAnimation(fig, animateAM, np.arange(1, 200), init_func=init)
    plt.legend(loc="upper left")
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)

    plt.show()

def init():
    print "hi"

def animateAM(i):
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

def animateABG(i):
    #global lines
    higha = mindWave.highAlpha
    lowa = mindWave.lowAlpha
    highb = mindWave.highBeta
    lowb = mindWave.lowBeta
    midg = mindWave.midGamma
    lowg = mindWave.lowGamma

    tmpList = lines[0].tolist()
    tmpList.append(higha)
    tmpList.remove(tmpList[0])
    lines[0] = np.array(tmpList)
    halpha.set_ydata(lines[0])

    tmpList = lines[1].tolist()
    tmpList.append(lowa)
    tmpList.remove(tmpList[1])
    lines[1] = np.array(tmpList)
    lalpha.set_ydata(lines[1])

    tmpList = lines[2].tolist()
    tmpList.append(highb)
    tmpList.remove(tmpList[2])
    lines[2] = np.array(tmpList)
    hbeta.set_ydata(lines[2])

    tmpList = lines[3].tolist()
    tmpList.append(lowb)
    tmpList.remove(tmpList[3])
    lines[3] = np.array(tmpList)
    lbeta.set_ydata(lines[3])

    tmpList = lines[4].tolist()
    tmpList.append(midg)
    tmpList.remove(tmpList[4])
    lines[4] = np.array(tmpList)
    mgamma.set_ydata(lines[4])

    tmpList = lines[5].tolist()
    tmpList.append(lowg)
    tmpList.remove(tmpList[5])
    lines[5] = np.array(tmpList)
    lgamma.set_ydata(lines[5])

    #line2 = mindWave.meditation
    return [halpha,lalpha,hbeta,lbeta,mgamma,lgamma]
