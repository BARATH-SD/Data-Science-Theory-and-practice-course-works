# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:11:46 2024

@author: barath
"""
"""Single x=[1,2,3,4,5] y=[10,20,30,40,50] n=1
   multi x=[(1,2),(2,3),(3,4)],y=[15,25,35]"""

import numpy as nm
import matplotlib.pyplot as plt

def grad_des(x,y):
    m=len(y)     # m samples
    try:
        n=len(x[0])  # n features
    except:
        n=1
    w=nm.zeros(n+1)
    def h(x,w):
        y_n=list()
        for i in range(m):
            y=w[0]
            if n>1:
                for j in range(1,n+1):
                    y+=x[i][j-1]*w[j]
            else:
                y+=w[1]*x[i]
            y_n.append(y)
        return y_n
    def J(x,y,w):
        y_n=h(x,w)
        j=0
        for i in range(m):
            j+=(y[i]-y_n[i])**2
        return j/(2*m)
    def grad_J(w):
        y_n=h(x,w)
        d_j=nm.zeros(n+1)
        if n==1:
            for i in range(m):
                d_j[0]+=(y_n[i]-y[i])/m
                d_j[1]+=(y_n[i]-y[i])*x[i]/m
        else:
            for i in range(m):
                d_j[0]+=(y_n[i]-y[i])/m
                for j in range(1,1+n):
                    d_j[j]+=(y_n[i]-y[i])*x[i][j-1]/m
        return d_j
    W=list()
   
    for i in range(1000):
        W.append(w-0.01*nm.array(grad_J(w)))
        w-=0.001*nm.array(grad_J(w))
        
    print('w =',w,'\nThe loss = ',J(x,y,w))
    
    def surface(W):
        a=[]
        b=[]
        for i in W:
            a.append(i[0])
            b.append(i[1])
        
        fig=plt.figure(figsize=(12,6))
        ax=fig.add_subplot(121,projection='3d')
        A,B=nm.meshgrid(a,b)
        w=[A,B]
        C=J(x,y,w)
        ax.plot_surface(A,B,C)
        plt.show()
        
    def contour(W):
        a=[]
        b=[]
        for i in W:
            a.append(i[0])
            b.append(i[1])
        A,B=nm.meshgrid(a,b)
        C=J(x,y,[A,B])
        fig=plt.figure(figsize=(12,6))
        ax=fig.add_subplot(111)
        cp=plt.contour(a,b,C)
        plt.clabel(cp)
        ax.set_xlabel('W0')
        ax.set_ylabel('W1')
        ax.set_title('Contour plot of J(w0,w1)')
        plt.show()
            
    if n==1:
        a=nm.linspace(0,20)
        b=w[0]+w[1]*a
        plt.plot(a,b,'r')
        plt.show()
        surface(W)
        contour(W)
    if n==2:
        a=nm.linspace(0,20)
        b=nm.linspace(0,20)
        A,B=nm.meshgrid(a,b)
        C=w[0]+w[1]*A+w[2]*B
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        ax.plot_surface(A,B,C)
        plt.show()
        

"""Q1"""
import csv
with open("univariate_linear_regression.csv",'r') as f:
    r=csv.reader(f)
    x=[]
    y=[]
    for i in r:
        try:
            x.append(float(i[0]))
            y.append(float(i[1]))
        except:
            pass
grad_des(x,y)

    


"""Q2"""
import csv
with open("heart.data.csv",'r') as f:
    r=csv.reader(f)
    x=[]
    y=[]
    for i in r:
        try:
            x.append([float(i[1]),float(i[2])])
            y.append(float(i[3]))
        except:
            pass
grad_des(x,y)




