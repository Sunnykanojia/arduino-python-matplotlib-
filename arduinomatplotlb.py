import serial
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
#import tkinterslider
plt.ion()
fig=plt.figure()
i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM3',9600)
ser.close()
ser.open()
while True:
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(float(data.decode()))
    plt.plot(x,y)
    #plt.plot(i, float(data.decode()))
    plt.xlabel("time")
    plt.ylabel("Voltage in mV")
    plt.title("Arduino clc solar panel")
    plt.grid(True,color="k",linestyle=":")
    #plt.style.use("")
    #plt.legend(loc=1)
    i += 1
    plt.show()
    plt.pause(0.0001)  # Note this correction




