# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:20:00 2024

@author: barath
"""

import numpy as nm
import csv
with open('Logistic_regression_ls.csv','r') as f:
    r=csv.reader(f)
    data=[]
    for i in r:
        data.append(i)
    data.pop(0)

X=[]
Y=[]
for i in data:
    X.append((float(i[0]),float(i[1])))
    Y.append(int(i[2]))

X=nm.array(X)
Y=nm.array(Y)
m=len(X) #m samples
n=len(X[0]) #n features

def sigmoid(x):
    return 1/(1+nm.e**(-x))
def sig_der(a):
    return a*(a-1)

#lets consider all the n hidden layer contain only 3 neurons each

def nn(x,y,N):
    w=[nm.random.rand(3,2)]
    b=[nm.random.rand(3)]
    for i in range(N-1):
        w.append(nm.random.randn(3,3))
        b.append(nm.random.randn(3))
    w.append(nm.random.randn(1,3))
    b.append(nm.random.randn(1))
    
    act=[x]
    for i in range(N+1):   # N layers+1 output layer
        z=nm.dot(act[-1],w[i].transpose())+b[i]
        a=sigmoid(z)
        act.append(a)
        
    d_w=[nm.zeros(i.shape) for i in w]
    d_b=[nm.zeros(i.shape) for i in b]
    error=act[-1].T-y
    error=error.T
    delta=error* sig_der(act[-1])
    d_w[-1]=nm.dot(delta.T,act[-2])
    d_b[-1]=delta.T

    for l in range(2,N+1):
        z=nm.dot(w[-l+1].T, delta.T)
        delta=z.T*sig_der(act[-l])
        d_w[-l]=nm.dot(delta.T,act[-l-1])
        d_b[-l]=delta.T
        
    for i in range(len(w)):
        w[i]-=0.01*d_w[i]
    #after updation
    A=[x]
    for i in range(N+1):  
        z=nm.dot(A[-1],w[i].transpose())+b[i]
        a=sigmoid(z)
        A.append(a)         
    return(A[-1])


def loss(N,X=X,Y=Y):      
    tr=int(m*0.7)
    val=int(m*0.15)
    
    X_tr=X[:tr]
    X_val=X[tr:tr+val]
    X_test=X[tr+val:m]   
    
    Y_tr=Y[:tr]
    Y_val=Y[tr:tr+val]
    Y_test=Y[tr+val:m]    

    a_tr=nn(X_tr,Y_tr,N)
    tr_loss=nm.mean((a_tr-Y_tr)**2)
    
    
    a_val=nn(X_val,Y_val,N)
    val_loss=nm.mean((a_val-Y_val)**2)
    
    a_test=nn(X_test,Y_test,N)
    test_loss=nm.mean((a_test-Y_test)**2)
    
    return tr_loss,val_loss,test_loss

N=5 # taking 5 hidden layers
tr_loss,val_loss,test_loss=loss(N)
print('Training loss   = ',tr_loss)
print('Validation loss = ',val_loss)
print('Test loss       = ',test_loss)


import matplotlib.pyplot as plt
ns=list(range(1,10))
tr_losses=[]
for i in ns:
    tr_losses.append(loss(i)[0])

plt.plot(ns,tr_losses,'g')
plt.xlabel('no. of hidden layers')
plt.ylabel('Training losses')
plt.title('Loss V/S n')


tr=int(m*0.7)
val=int(m*0.15)

X_tr=X[:tr]
X_val=X[tr:tr+val]
X_test=X[tr+val:m]   

Y_tr=Y[:tr]
Y_val=Y[tr:tr+val]
Y_test=Y[tr+val:m]
N=5
a_test=nn(X_test,Y_test, N)
y_pred=[]
for i in a_test:
    if i>0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)
y_pred=nm.array(y_pred)

tp=nm.sum((Y_test==1) & (y_pred==1))
fp=nm.sum((Y_test==0) & (y_pred==1))
fn=nm.sum((Y_test==1) & (y_pred==0))
tn=nm.sum((Y_test==0) & (y_pred==0))

p=tp/(tp+fp) if tp+fp>0 else 0
r=tp/(tp+fn)
f1=2*p*r/(p+r)
a=(tp+tn)/(tp+tn+fp+fn)

print("Precision:",p)
print("Recall:",r)
print("F1-Score:",f1)
print("Accuracy:",a)






