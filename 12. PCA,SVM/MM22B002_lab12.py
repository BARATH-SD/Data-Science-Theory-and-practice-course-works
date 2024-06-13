# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:07:20 2024

@author: barath
"""
"""Q1"""
import matplotlib.pyplot as plt
import numpy as nm
from sklearn import datasets,decomposition,svm
from sklearn.inspection import DecisionBoundaryDisplay
nm.random.seed(5)

#1.loading the dataset

iris=datasets.load_iris()
x=iris.data[:,:2]    #taking 2 features
y=iris.target  

#2.visualising the dataset

plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.gist_rainbow)
plt.xlabel('Sepal length(cm)')
plt.ylabel('Sepal width(cm)')
plt.title('Iris Dataset')
plt.show()

#3.Splitting the data into training and testing sets 
#taking 70% for training
n=len(x)
n_tr=int(n*0.7)
i=nm.arange(n)
nm.random.shuffle(i)
x_train,x_test=x[i[:n_tr]],x[i[n_tr:]]
y_train,y_test=y[i[:n_tr]],y[i[n_tr:]]
plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap=plt.cm.gist_rainbow)
plt.xlabel('Sepal length(cm)')
plt.ylabel('Sepal width(cm)')
plt.title('Training Dataset')
plt.show()

#4.Initialising SVM
SVM=svm.SVC(kernel='linear', C=1.0, random_state=42)
SVM.fit(x_train,y_train)

#5.Testing the model

y_pred = SVM.predict(x_test)
plt.scatter(x_test[:,0],x_test[:,1],c=y_test,cmap=plt.cm.gist_rainbow)
plt.scatter(x_test[:,0],x_test[:,1],c=y_pred,cmap=plt.cm.gist_rainbow)

correct=sum(y_pred == y_test)
total=len(y_test)
accuracy = correct / total

print("Accuracy:", accuracy)



#1.loading the dataset
digits = datasets.load_digits()
X = digits.data
y = digits.target

#2.visualising the dataset
fig,axes=plt.subplots(2,5, figsize=(10, 5))
for ax,image,label in zip(axes.flat, digits.images, digits.target):
    ax.imshow(image, cmap=plt.cm.gray_r)
    ax.set_title(f"Label: {label}")
    ax.axis('off')
plt.show()

#3.Splitting the data into training and testing sets 

n=len(X)
n_train=int(0.7*n)
indices=nm.arange(n)
nm.random.shuffle(indices)
X_train,X_test=X[indices[:n_train]],X[indices[n_train:]]
y_train,y_test=y[indices[:n_train]],y[indices[n_train:]]

# Initialize and train the SVM model
SVM=svm.SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
SVM.fit(X_train, y_train)

# Testing the model
y_pred = SVM.predict(X_test)
correct=sum(y_pred==y_test)
total=len(y_test)
accuracy = correct / total

print("Accuracy:", accuracy)


"""Q2"""

#eigen decompostion

iris=datasets.load_iris()

X=iris.data
Y=iris.target

X_mean=nm.mean(X,axis=0)
X_stand=X-X_mean
cov_mat=nm.cov(X_stand,rowvar=False)
egnvalues,egnvectors=nm.linalg.eig(cov_mat)

sorted_indices = nm.argsort(egnvalues)[::-1]
eigenvalues = egnvalues[sorted_indices]
egnvectors = egnvectors[:, sorted_indices]

#we will take the first three components of each egnvector
X_pca=nm.dot(X_stand,egnvectors[:,:3])


fig=plt.figure()
ax = fig.add_subplot(111, projection="3d", elev=50, azim=140)
ax.set_position([0, 0, 0.95, 1])

for name, label in [("Setosa", 0), ("Versicolour", 1), ("Virginica", 2)]:
    ax.text3D(
        X_pca[Y == label, 0].mean(),
        X_pca[Y == label, 1].mean() + 1.5,
        X_pca[Y == label, 2].mean(),
        name,
        horizontalalignment="center",
        bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
    )

Y = nm.choose(Y, [1, 2, 0]).astype(float)
ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=Y, cmap=plt.cm.nipy_spectral, edgecolor="k")

ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])

plt.show()

#PCA method

iris=datasets.load_iris()
x=iris.data
y=iris.target
fig=plt.figure()
ax = fig.add_subplot(111, projection="3d", elev=50, azim=140)
ax.set_position([0, 0, 0.95, 1])

pca=decomposition.PCA(n_components=3)
pca.fit(x)
x=pca.transform(x)


for name, label in [("Setosa", 0), ("Versicolour", 1), ("Virginica", 2)]:
    ax.text3D(
        x[y == label, 0].mean(),
        x[y == label, 1].mean() + 1.5,
        x[y == label, 2].mean(),
        name,
        horizontalalignment="center",
        bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
    )

y = nm.choose(y, [1, 2, 0]).astype(float)
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y, cmap=plt.cm.nipy_spectral, edgecolor="k")

ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])

plt.show()

print('For comparison')
print('The first 5 values,by eigen decomposition are :\n',X_pca[:5])
print()
print('The first five values, by pca method are :\n',x[:5])