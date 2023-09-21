import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from sin import mySin
a0=math.radians(45)
w=0
g=-9.81
m=1
l=1
dt=.1
def midP(a,w):
    xs=[]
    eks=[]
    eps=[]
    ecs=[]
    tab=[]
    t=0
    global g,m,l,dt
    while t<=22.9:
        e = g / l * mySin(a)
        w1 = w + e * dt / 2
        a1 = a + w1 * dt
        a2 = a + w * dt / 2
        e1 = g / l * mySin(a2)
        w2 = w + e1 * dt
        b = a - math.pi / 2
        x = l * -mySin(b)
        y = l * mySin(b)
        h = y + l
        ep = abs(m * g * h)
        ek = m * math.pow(l * w, 2) / 2
        ec = ep + ek
        xs.append(t)
        eks.append(ek)
        eps.append(ep)
        ecs.append(ec)
        tab.append([t,a,w,x,y,ep,ek,ec])
        t+=dt
        a = a1
        w = w2
    print(tabulate(tab,headers=["t","a","w","x","y","ek","ep","ec"]))
    plt.plot(np.array(xs), np.array(eks))
    plt.plot(np.array(xs), np.array(eps))
    plt.plot(np.array(xs), np.array(ecs))
    plt.show()
def rk4(a,w):
    tab=[]
    xs = []
    eks = []
    eps = []
    ecs = []
    t=0
    global g,m,l,dt
    while t<= 22.9:
        e = g / l * mySin(a)
        i1=a+w*dt/2
        k2a=w+e*dt/2
        k2w=g/l*mySin(i1)
        i2=a+k2a*dt/2
        k3a=w+k2w*dt/2
        k3w=g/l*mySin(i2)
        i3=a+k3a*dt
        k4a=w+k3w*dt
        k4w=g/l*mySin(i3)
        da=(w+k2a*2+k3a*2+k4a)/6*dt
        dw=(e+2*k2w+k3w*2+k4w)/6*dt
        b=a-math.pi/2
        x=l*-mySin(b)
        y=l*mySin(b)
        h=y+l
        ep=abs(m*g*h)
        ek=m*math.pow(l*w,2)/2
        ec=ep+ek
        xs.append(t)
        eks.append(ek)
        eps.append(ep)
        ecs.append(ec)
        tab.append([t,a,w,x,y,ep,ek,ec])
        t+=dt
        a+=da
        w+=dw

    print(tabulate(tab, headers=["t","a","w","x","y","ek","ep","ec"]))
    plt.plot(np.array(xs), np.array(eks))
    plt.plot(np.array(xs), np.array(eps))
    plt.plot(np.array(xs), np.array(ecs))
    plt.show()
midP(a0,w)
rk4(a0,w)

