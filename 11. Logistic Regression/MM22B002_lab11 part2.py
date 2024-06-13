# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:41:30 2024

@author: barath
"""

import csv
with open("Logistic_regression_ls.csv",'r') as f:
    r=csv.reader(f)
    x=[]
    y=[]
    for i in r:
        try:
            x.append([float(i[0]),float(i[1])])
            y.append(float(i[2]))
        except:
            pass

import numpy as nm
import matplotlib.pyplot as plt

x1=[]
x2=[]
for i in x:
    x1.append(i[0])
    x2.append(i[1])
    

X1=[]
X2=[]
X3=[]
X4=[]
for i in range(len(y)):
    if y[i]==0:
        X1.append(x1[i])
        X2.append(x2[i])
    elif y[i]==1:
        X3.append(x1[i])
        X4.append(x2[i])
        
plt.plot(X1,X2,'om')
plt.plot(X3,X4,'oc')    
    
m=len(y)
w=nm.zeros(3) #w_o w_1 and w_2
def h(x,w):
    y_n=list()
    for i in x:
        y_n.append(1/(1+(nm.e**(-(w[0]+w[1]*i[0]+w[2]*i[1])))))
    return y_n

def J(x,y,w):
   y_n=h(x,w)
   j=0
   for i in range(m):
       if y[i]==0:
           j+=(-nm.log(1-y_n[i]))
       else:
           j+=(-nm.log(y_n[i]))
   return j/m
    
def grad_j(x,y,w):
    y_n=h(x,w)
    d_j=nm.zeros(3)
    for i in range(m):
        d_j[0]+=(y_n[i]-y[i])/m
        d_j[1]+=(y_n[i]-y[i])*x[i][0]/m
        d_j[2]+=(y_n[i]-y[i])*x[i][1]/m
    return d_j

W=[]
for i in range(5000):
    j=J(x,y,w)   
    W.append(w)
    w=w-0.01*nm.array(grad_j(x,y,w))
    if J(x,y,w)>j:
        break
print('w =',w,'\nThe loss = ',J(x,y,w))


X=nm.linspace(0,10)
Y=[]
for i in X:
    Y.append((-w[0]-w[1]*i)/w[2])
plt.plot(X,Y,'r')











