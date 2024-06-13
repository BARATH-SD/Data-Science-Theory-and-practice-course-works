# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:52:59 2024

@author: barath
"""

"""Q1"""
#a 
# J(w) = w^2 + (54/w) let a=1 b=10 n=100
def J(w):
    return(w**2+52/w)

def brkt(a,b,n):
    x=(b-a)/n
    w1=a
    w2=w1+x
    w3=w2+x
    for i in range(n):
        if J(w1)>=J(w2)<=J(w3):
                return w1, w3
        else:
            w1=w2
            w2=w3
            w3=w2+x
            
c1,c2=(brkt(1,10,100))
#interval halving method

def inrtvl(a,b):
    x=b-a
    wm=(a+b)/2
    w1=a+x/4
    w2=b-x/4
    if J(w1)<J(wm):
        b=wm
        wm=w1
    elif J(w2)<J(wm):
        a=wm
        wm=w2
    else:
        a=w1
        b=w2
    x=b-a
    e=0.001
    if -e<=x<=e:
        print('The approx. min. is',(a+b)/2)
        print('The min. value =',J((a+b)/2))
    else:
        inrtvl(a,b)

inrtvl(c1,c2)

#B  Newton-Raphson method
def J1(w):
    return(w*2-52/w**2)
def J2(w):
    return(2+104/w**3)

def newton(w):
    w-=J1(w)/J2(w)
    e=0.001
    if -e<=J1(w)<=e:
        print('The approx. min. is',w)
    else:
        newton(w)
        
newton(1)

"""Q2"""
# J(w1, w2) = (w1 - 10)^2 + (w2 - 10)^2
import numpy as nm
import matplotlib.pyplot as plt
x=nm.linspace(5,15,100)
y=nm.linspace(5,15,100)
X,Y=nm.meshgrid(x,y)
Z=(X-10)**2+(Y-10)**2

fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_zlabel('J (w1,w2)')
ax.set_title('z=(w1-10)^2+(w2-10)^2')

ax=fig.add_subplot(122)
cp=plt.contour(x,y,Z)
plt.clabel(cp)
ax.set_xlabel('W1')
ax.set_ylabel('W2')
ax.set_title('Contour plot of J(w1,w2)')
plt.colorbar()
plt.show()


"""Q3"""
# (w1 - 10 )^2 + (w2 - 10)^2
# start point (2,1)
# direction (2, 5)
s=nm.linspace(1,15,100)
x=2+2*s
y=1+5*s

X,Y=nm.meshgrid(x,y)
Z=(X-10)**2+(Y-10)**2

fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_zlabel('J (w1,w2)')
ax.set_title('z=(w1-10)^2+(w2-10)^2')

ax=fig.add_subplot(122)
cp=plt.contour(x,y,Z)
plt.clabel(cp)
ax.set_xlabel('W1')
ax.set_ylabel('W2')
ax.set_title('Contour plot of J(w1,w2)')
plt.show()


def J(x,y):
    return((x-10)**2+(y-10)**2)

def brkt_m(a,b,n):
    c=(b-a)/n
    w1=nm.array((2,1))
    w2=w1+c*nm.array((2,5))
    w3=w2+c*nm.array((2,5))
    for i in range(n):
        if J(*w1)>=J(*w2)<=J(*w3):
                return w1, w3
        else:
            w1=w2
            w2=w3
            w3=w2+c*nm.array((2,5))
            
w1,w2=brkt_m(0,10,100)
print('The min. lies between ',w1,'and',w2)
c1=(w1-nm.array((2,1)))/nm.array((2,5))
c1=c1[0]
c2=(w2-nm.array((2,1)))/nm.array((2,5))
c2=c2[0]
print('The value of alpha lies between',c1,'and',c2)

def inrtvl_m(a,b):
    x=b-a
    wm=(a+b)/2
    w1=a+x/4
    w2=b-x/4
    if J(*(nm.array((2,1))+w1*nm.array((2,5))))<J(*(nm.array((2,1))+wm*nm.array((2,5)))):
        b=wm
        wm=w1
    elif J(*(nm.array((2,1))+w2*nm.array((2,5)))<J(*(nm.array((2,1)))+wm*nm.array((2,5)))):
        a=wm
        wm=w2
    else:
        a=w1
        b=w2
    x=b-a
    e=0.001
    if -e<=x<=e:
        print((a+b)/2)
        c=(a+b)/2
        x,y=nm.array((2,1))+c*nm.array((2,5))
        print('The min. value occurs at',(x,y))
        print('The min. value =',J(x,y))
        
    else:
        inrtvl_m(a,b)
        
inrtvl_m(c1,c2)


