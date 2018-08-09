import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.patches as patches
import numpy as np
from numpy.polynomial import Polynomial

def contains_border(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            if(im_data[j][i][0] != 1):
                return True

def draw_squares(height, width, size, plot = False):
    n_x = int(width/size)
    n_y = int(height/size)
    N = 0
    x_start = int((width - n_x*size)/2)
    y_start = int((height - n_y*size)/2)
    for i in range(n_x):
        for j in range(n_y):
            if(contains_border(x_start + i*size, y_start + j*size, size)):
                N += 1
                if(plot):
                    rect = patches.Rectangle((x_start + i*size, y_start + j*size),size,size,linewidth=1,edgecolor='r',facecolor='none')
                    ax.add_patch(rect)
                
    return N

image_name = 'LVA.png'
im_data=img.imread(image_name)


####This part creates a single plot showing active squares
##side= 25
##fig,ax = plt.subplots(1)
##ax.imshow(im_data)
##ax.axes.get_xaxis().set_visible(False)
##ax.axes.get_yaxis().set_visible(False)
##val = draw_squares(np.shape(im_data)[0], np.shape(im_data)[1], side, True)
##ax.text(412, 20, 'N = ' + str(val), fontsize=12)
##ax.text(412, 45, 'L = ' + str(side), fontsize=12)

size = []
num = []

for side_length in range (50, 5, -5):
    num.append(draw_squares(np.shape(im_data)[0], np.shape(im_data)[1], side_length))
    size.append(side_length)
    
x = np.log(size)
y = np.log(num)
coefs, cov = np.polyfit(x, y, 1, cov = True)
print(coefs)
print(cov)
f = np.poly1d(coefs)
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)
plt.plot(x, y, 'ro',label = 'novērotie punkti')
plt.plot(x_new, y_new, '--', label = 'lineārās regresijas līkne')
plt.xlabel("ln(L[px])")
plt.ylabel("ln(N)")
plt.legend()
plt.show()



