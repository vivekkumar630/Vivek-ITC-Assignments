from math import *
# create a for loop
for i in range(0, 360, 15):
    # then print the sine and cosine of the angles
    print(i, '---', round(sin(i), 4), round(cos(i),4))
