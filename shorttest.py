from NK_Interface import NK_Interface
import numpy
import numpy.fft
from classifier import Classifier


dir_list = [0,3,2,1,2,0]
gui = NK_Interface(1,0,1, dir_list)
gui.init_calib()

k = gui.return_data()
c = Classifier(False)
data = []
for a in k:
    data.append(c.createFeatureVector(a[0],a[1]))



c.train(data)
