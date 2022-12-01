import matplotlib.pyplot as plt
import numpy as np
import math


x = []
y = []


readFile = open('DS0.txt', 'r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotPair in sepFile:
    xAndY = plotPair.split(' ')
    y.append(int(xAndY[0]))
    x.append(int(xAndY[1]))


  
for i in range(1,len(y)):
    y[i]=(x[i]*math.sin(40)+y[i]*math.cos(40))+480
for j in range(1,len(x)):
    x[j]=(x[j]*math.cos(40)-y[j]*math.sin(40))+480
for i in range(1,len(y)):
    y[i]=(y[i]/((100/960)+1))
for j in range(1,len(x)):
    x[j]=(x[j]/((100/540)+1))


px = 1/plt.rcParams['figure.dpi']
plt.subplots(figsize=(960*px, 540*px))
plt.scatter(x, y)
plt.savefig('LAB4.png')
plt.show()
