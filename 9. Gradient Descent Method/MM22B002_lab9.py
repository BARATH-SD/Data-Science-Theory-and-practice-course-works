# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:09:43 2024

@author: barath
"""

"""Q2"""
#J(x1, x2) = (x1^2+x2−11)^2+(x1+x2^2−7)^2    
#A
def J(x,y):
    return(x**2+y-11)**2+(x+y**2-7)**2
import numpy as nm
import matplotlib.pyplot as plt

x=nm.linspace(-10,10,100)
y=nm.linspace(-10,10,100)
X,Y=nm.meshgrid(x,y)
Z=(X**2+Y-11)**2+(X+Y**2-7)**2

fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121,projection='3d')
ax.plot_surface(X,Y,Z)
ax=fig.add_subplot(122)
cp=plt.contour(x,y,Z)
plt.clabel(cp)

def detJ(x,y):
    h=0.00001
    return ((J(x+h,y)-J(x-h,y))/(2*h)),((J(x,y+h)-J(x,y-h))/(2*h))

def mag(x,y):
    return(x**2+y**2)**0.5

def grad_descent(x,y,alpha=0.01,k=1):
    xl=[x]
    yl=[y]
    a=alpha
    k+=1
    n=nm.array((x,y))
    detj=nm.array(detJ(x,y))
    X,Y=n-a*detj
    xl.append(X)
    yl.append(Y)
    if mag(*detj)<=0.001:
        print('One of the minimum occurs at :',X,Y)
    elif mag(*(detj*nm.array(detJ(X,Y))))<=0.001:
        print('One of the minimum occurs at :',X,Y)
    elif mag(*(n-[X,Y]))/mag(*n)<=0.001:
        print('One of the minimum occurs at :',X,Y)
        x,y=xl,yl
        X,Y=nm.meshgrid(x,y)
        Z=(X**2+Y-11)**2+(X+Y**2-7)**2
        fig=plt.figure(figsize=(12,6))
        ax=fig.add_subplot(121,projection='3d')
        ax.plot_surface(X,Y,Z)
        ax=fig.add_subplot(122)
        cp=plt.contour(x,y,Z)
        plt.clabel(cp)
        plt.show()
    elif k>100:
        print('After 100 iterations :',X,Y)
    else:
        grad_descent(X,Y,a,k)

grad_descent(3,3)
grad_descent(-3,3)
grad_descent(-3,-3)
grad_descent(3,-3)

#B For varying alpha

def brkt_m(x,y,n=100):
    c=0.01
    w1=nm.array((x,y))
    w2=w1-c*nm.array(detJ(*w1))
    w3=w2-c*nm.array(detJ(*w1))
    for i in range(n):
        if J(*w1)>=J(*w2)<=J(*w3):           
            W=(w1+w3)/2
            return nm.array((nm.array((x,y))-W)/(detJ(x,y))).mean()
        else:
            w1=w2
            w2=w3
            w3=w2-c*nm.array(detJ(x,y))


def grad_alpha(x,y,k=1):
    a=brkt_m(x,y)
    k+=1
    n=nm.array((x,y))
    detj=nm.array(detJ(x,y))
    X,Y=n-a*detj    
    if mag(*detj)<=0.001:
        print('One of the minimum occurs at :',X,Y)
    elif mag(*(detj*nm.array(detJ(X,Y))))<=0.001:
        print('One of the minimum occurs at :',X,Y)
    elif mag(*(n-[X,Y]))/mag(*n)<=0.001:
        print('One of the minimum occurs at :',X,Y)
    elif k>100:
        print('After 100 iterations :',X,Y)
    else:
        grad_alpha(X,Y,k)
    


grad_alpha(3,3)
grad_alpha(-3,3)
grad_alpha(-3,-3)
grad_alpha(3,-3)













