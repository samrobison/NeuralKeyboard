from NK_Interface import NK_Interface
import numpy
import numpy.fft
from classifier import Classifier


dir_list = [0,1,2,3]
gui = NK_Interface(0,1,1, dir_list)
gui.init_calib()

k = gui.return_data()
c = Classifier(False)
data = []
for a in k:
  data.append(c.createFeatureVector(a[0],[1]))
c.train(data)
