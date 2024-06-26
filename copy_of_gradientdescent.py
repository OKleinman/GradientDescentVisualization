# -*- coding: utf-8 -*-

! pip install kaggle

! mkdir ~/.kaggle

!cp /content/drive/MyDrive/kaggle.json ~/.kaggle/kaggle.json

! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download hellbuoy/car-price-prediction

! unzip car-price-prediction.zip


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CarPrice_Assignment.csv")
df = df[['enginesize','horsepower','price']]
df.head()


from mpl_toolkits import mplot3d
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x=df["enginesize"].to_numpy()
y=df["horsepower"].to_numpy()

plt.scatter(x,y)

X=df["enginesize"].to_numpy()
# y=df["horsepower"].to_numpy()
Y=df["price"].to_numpy()

# Building the model
m = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 10  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent
for i in range(epochs):
    Y_pred = m*X + c  # The current predicted value of Y
    D_c = (-2/n) * sum(Y[i] - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c

print(m,c)

x

slope=0
intercept=0
learningRate=.01

epochs=1000

import random
import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
from mpl_toolkits import mplot3d
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

a = []
b = []
Z = []

# def cost(t0, a, t1, b):
#   return t0*a + t1*b

def fun(x, y):
  # return x**2 - y**2
  return ((x ** 2) -(20*x) + 100 + (y ** 2) + (10*y) + 25)
  # return function with local minima

  # for each m and b value, calculute the residuals of all points to the line defined by this m and b value and have the value of the
  # mean of the sum of the residuals as the z value

for i in range(10):
  x = np.arange(2.0, 16.0, .1)
  y = np.arange(-12.0, 6.0, .1)
# print(a)
# print(b)
# print(y)
a=np.array(x)
b=np.array(y)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.scatter(3.6, -0.12, fun(3.6, -0.20), c="blue")
ax.scatter(4.88, -1.16, fun(4.88, -1.16), c="black")
ax.scatter(5.90, -1.93, fun(5.90, -1.93), c="black")
ax.scatter(6.72, -2.54, fun(6.72, -2.54), c="black")
ax.scatter(7.38, -3.03, fun(7.38, -3.03), c="black")
ax.scatter(7.90, -3.43, fun(7.90, -3.43), c="black")
ax.scatter(8.32, -3.74, fun(8.32, -3.74), c="black")
ax.scatter(8.66, -3.99, fun(8.66, -3.99), c="black")
# #... to x sub n
ax.scatter(9.999651501222615, -4.999738874606919, fun(9.999651501222615, -4.999738874606919), c="red", edgecolor="black")

info = {}

epochs = 10001
learning_rate = 0.1
stopping_threshold = .0001

def dx(x):
  # derive cost function with respect to a, plug in positonA and return value.
  # x ** 2 -(4*x) + 4 + (y ** 2)
  h = 0.00000001
  derivative = (fun(x + h, 0) - fun(x, 0)) / h
  # Returns the slope to the third decimal
  info[f'{info_increment}_dx']=derivative
  return derivative

def dy(y):
  # derive cost function with respect to a, plug in positonA and return value.
  h = 0.00000001
  derivative = (fun(0, y + h) - fun(0, y)) / h
  # Returns the slope to the third decimal
  info[f'{info_increment}_dy']=derivative
  return derivative

start_pos = [0,0];
info_increment = 0

while True:
    start_x = random.randint(2, 16)
    start_y = random.randint(-12, 6)

    # if point (start x, start y) have a gradient of 0 it isnt stuck in a maximum and if it starts on a minimum we still change it
    # because it will find the minimum eventually
    if dx(start_x)>.0001 or dy(start_y)>.0001:
        start_pos = [start_x, start_y]
        break


gd_points = []

for i in range(epochs):
  pos = start_pos

  dwrx = dx(pos[0])*learning_rate*-1
  dwry = dy(pos[1])*learning_rate*-1

  pos[0] += dwrx
  pos[1] += dwry


  if abs(dwrx)<stopping_threshold and abs(dwry)<stopping_threshold:
    print(f"Stopped early at point: {pos[0], pos[1], i}")
    gd_points.append([pos[0], pos[1], fun(pos[0], pos[1]), i, dwrx, dwry])
    break

  if i % 1 == 0:
    print(pos[0], pos[1])
    gd_points.append([pos[0], pos[1], fun(pos[0], pos[1]), i, dwrx, dwry])

  info_increment += 1;

print(gd_points)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.scatter(start_x, start_y, fun(start_x, start_y), c="blue")
for point in gd_points[1:-2]:
  ax.scatter(point[0], point[1], point[2], c="red")
ax.scatter(gd_points[-1][0], gd_points[-1][1], gd_points[-1][2], c="green")
ax.set_title('Cost Function Minimization by Gradient Descent')
ax.set_xlabel('X Coffiecients')
ax.set_ylabel('Y Coefficients')
ax.set_zlabel('Cost/Error')
ax.dist = 11
plt.show

print(info["0_dx"])
print(info["0_dy"])


"""# Optimizaion and improvement"""

import math as math

def c(x, y):
  return ((x ** 2) + np.sin((y ** 2)))

for i in range(10):
  x = np.arange(-2.0, 2.0, .01)
  y = np.arange(-3.0, 1.0, .01)

a=np.array(x)
b=np.array(y)
X, Y = np.meshgrid(x, y)
zs = np.array(c(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

xmin = -2
ymin = -3
xmax = 2
ymax = 1
descent_iterations = 8

epochs = 10001
learning_rate = 0.01
stopping_threshold = .000000001

def dx(positionA):
  h = 0.00000001
  top = c(positionA + h, 0) - c(positionA, 0)
  bottom = h
  slope = top / bottom
  return float(slope)

def dy(positionB):
  h = 0.00000001
  top = c(0, positionB + h) - c(0, positionB)
  bottom = h
  slope = top / bottom
  return float(slope)

start_pos = [0,0]
best_min = [0,0]
gd_index = 0
gd_points = []

for count in range(descent_iterations):
  while True:
      start_x = random.randint(xmin, xmax)
      start_y = random.randint(ymin, ymax)
      if dx(start_x)>.0001 or dy(start_y)>.0001:
          start_pos = [start_x, start_y]
          break


  best_min_range = [0,0]
  best_descent = []

  for i in range(epochs):
    pos = start_pos


    dwrx = dx(pos[0])*learning_rate*-1
    dwry = dy(pos[1])*learning_rate*-1

    pos[0] += dwrx
    pos[1] += dwry

    if abs(dwrx)<stopping_threshold and abs(dwry)<stopping_threshold:
      print(f"Stopped early at point: {pos[0], pos[1], i}")
      gd_points.append([pos[0], pos[1], c(pos[0], pos[1]), i])
      gd_index+=1
      if c(pos[0], pos[1]) < fun(best_min[0], best_min[1]):
        best_min = [pos[0], pos[1]]
        best_min_range[1] = gd_index
      else:
        best_min_range[0] = gd_index+1
      break

    if i % 50 == 0:
      print(pos[0], pos[1])
      gd_points.append([pos[0], pos[1], c(pos[0], pos[1]), i])
      best_descent.append([pos[0], pos[1], c(pos[0], pos[1]), i])

    if i == (epochs-1):
      print(f'Reached final number of epochs ({epochs}) at: {pos[0]},{pos[1]}')
      if c(pos[0], pos[1]) < c(best_min[0], best_min[1]):
        best_min = [pos[0], pos[1]]
      else:
        best_descent.clear()
      break

print(gd_points)
print(f'BEST MIN: {best_min}')
for i in range(best_min_range[0],best_min_range[1]):
  best_descent.append(gd_points[i])
print(best_descent)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
for point in gd_points:
  ax.scatter(start_x, start_y, c(start_x, start_y), c="blue")
  ax.scatter(point[0], point[1], c(point[0], point[1]), c="red")
ax.set_title('surface')
plt.show

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
for point in best_descent:
  ax.scatter(start_x, start_y, c(start_x, start_y))
  ax.scatter(point[0], point[1], point[2], c="red")
plt.show

print(best_descent[-1])
