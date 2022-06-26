from dis import dis
import numpy as np
import pylab
import scipy.stats as stats
from matplotlib import pyplot as plt
from time import sleep

n1 = np.random.normal(loc =0,scale =1,size =100)

np.percentile(n1,100)

n1 = np.random.normal(loc =20,scale =3,size =100)

stats.probplot(n1,dist="norm",plot=pylab)
# sleep(10)
plt.show()