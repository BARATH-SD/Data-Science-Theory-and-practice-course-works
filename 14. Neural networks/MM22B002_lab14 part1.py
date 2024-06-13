# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:15:47 2024

@author: barath
"""
import numpy as nm
import random
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

#initialisation asuming 3 neurons
#layer 1

w1=nm.array((random.random(),random.random()))
w2=nm.array((random.random(),random.random()))
w3=nm.array((random.random(),random.random()))

b=nm.array((0,0,0))    #let the bias be 0
w_1=nm.array((w1,w2,w3))

print('X',X.shape)
print('w_1',w_1.shape)
z_1=nm.dot(X,w_1.transpose())+b
a_1=sigmoid(z_1)

print('a_1',a_1.shape)

#layer 2
w_2=nm.random.randn(3,3)
z_2=nm.dot(a_1,w_2.transpose())+b
a_2=sigmoid(z_2)
print('a_2',a_2.shape)

# output
w_3=nm.random.randn(1,3)
z_3=nm.dot(a_2,w_3.transpose())+0
a_3=sigmoid(z_3)
print('a_3',a_3.shape)



def J(y,a_3):
    j=0
    for i in range(m):
        if y[i]==0:
            j+=(-nm.log(1-a_3[i]))
        else:
            j+=(-nm.log(a_3[i]))
    print('Cross entropy',float(j/m))

def mse(y,a_3):
    print('MSE',nm.mean((y-a_3)**2))
    
print('Using sigmoid as activation')
J(Y,a_3)    
mse(Y,a_3)


#relu
z_1r=nm.dot(X,w_1.transpose())+b
a_1r=nm.maximum(0,z_1r)
z_2r=nm.dot(a_1r,w_2.transpose())+b
a_2r=nm.maximum(0,z_2r)
z_3r=nm.dot(a_2,w_3.transpose())+0
a_3r=nm.maximum(0,z_3r)

print('Using ReLU')  
mse(Y,a_3r)

#using tanh

z_1=nm.dot(X,w_1.transpose())+b
a_1=nm.tanh(z_1)
z_2=nm.dot(a_1,w_2.transpose())+b
a_2=nm.tanh(z_2)
z_3=nm.dot(a_2,w_3.transpose())+0
a_3=sigmoid(z_3)

print('Using tanh as activation')
J(Y,a_3)    
mse(Y,a_3)

y_pred=[]
for i in a_3:
    if i>0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)
y_pred=nm.array(y_pred)

tp=nm.sum((Y==1) & (y_pred==1))
fp=nm.sum((Y==0) & (y_pred==1))
fn=nm.sum((Y==1) & (y_pred==0))
tn=nm.sum((Y==0) & (y_pred==0))

p=tp/(tp+fp) if tp+fp>0 else 0
r=tp/(tp+fn)
f1=2*p*r/(p+r)
a=(tp+tn)/(tp+tn+fp+fn)

print("Precision:",p)
print("Recall:",r)
print("F1-Score:",f1)
print("Accuracy:",a)