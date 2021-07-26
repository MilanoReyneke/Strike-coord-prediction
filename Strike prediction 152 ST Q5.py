#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''In this question we were asked to predict where 4 missiles would strike given some trajectory data.
The coordinates were also calculated. This was a question from a test in mathematical modeling'''





xy_data = [
    (-120.05237090694067, 930.1249822492173),
    (-981.2467441746327, 521.6488875435189),
    (-359.80045288785055, 737.578109575062),
    (-940.6364671538131, 547.611479069524),
    (-1015.3468441889291, 498.1838997403989),
    (-409.83121804149187, 751.0539913236357),
    (-260.3518352797322, 328.52995061690956),
    (-125.51183349571542, 223.08350255310657),
    (-310.8965520716082, 1154.286594651248),
    (-434.12309575042264, 1238.8717578489673),
    (-353.37478290273424, 735.5475531968729),
    (-327.8727423525763, 726.786582033227),
    (-158.9656143665593, 251.81885152562012),
    (-298.94051309200603, 1143.5846883538977),
    (-153.07014470542418, 246.88573104529192),
    (-1071.010317126787, 456.59902579881594),
    (-224.4768723154321, 1066.802551041043),
    (-335.83748977249365, 1175.2133085235469),
    (-867.2158258312104, 589.0893605484719),
    (-216.71153866998225, 297.4379008839453),
    (-180.76738965402572, 1013.7207387339963),
    (-129.18870685834176, 226.33753305515287),
    (-110.4150588626816, 915.7930401964322),
    (-1089.3848278908222, 441.97278923631234),
    (-488.0495341770337, 763.6873577080687),
    (-327.93152405884706, 726.8035452146653),
    (-396.6229002627526, 747.8975635439459),
    (-99.77054758133697, 199.7735484192477),
    (-864.6036319177803, 590.401903887385),
    (-132.8813268900396, 229.5515697656306),
    (-308.42210321283085, 719.3677882258944),
    (-177.1530139796593, 266.75458246088164),
    (-454.6982287339466, 759.5484052750057),
    (-292.25374018107647, 1137.3611630427215),
    (-995.9353796179176, 511.72078418615683),
    (-1059.772663500067, 465.3141333990594)
]    
x_data, y_data = zip(*xy_data)

import matplotlib.pyplot as plt

fig, ax  = plt.figure(), plt.axes()

ax.plot(x_data, y_data, "o")
plt.show()


# In[2]:


missile_A_data = []
missile_B_data = []
missile_C_data = []
missile_D_data = []

for i in range(len(xy_data)):
    if 0 < xy_data[i][1] and 400 >= xy_data[i][1]:
        missile_D_data.append(xy_data[i])
    elif 400 < xy_data[i][1] and 650 >= xy_data[i][1]:
         missile_C_data.append(xy_data[i])
    elif 650 < xy_data[i][1] and 800 >= xy_data[i][1]:
         missile_B_data.append(xy_data[i])
    else:
         missile_A_data.append(xy_data[i])


# In[3]:


import numpy as np

X_missA, Y_missA = zip(*missile_A_data)
a_missA, b_missA, c_missA = np.polyfit(X_missA, Y_missA, 2)

X_missB, Y_missB = zip(*missile_B_data)
a_missB, b_missB, c_missB = np.polyfit(X_missB, Y_missB, 2)

X_missC, Y_missC = zip(*missile_C_data)
a_missC, b_missC, c_missC = np.polyfit(X_missC, Y_missC, 2)

X_missD, Y_missD = zip(*missile_D_data)
a_missD, b_missD, c_missD = np.polyfit(X_missD, Y_missD, 2)

print(a_missA, b_missA, c_missA)
print(a_missB, b_missB, c_missB)
print(a_missC, b_missC, c_missC)
print(a_missD, b_missD, c_missD)


# In[4]:


import sympy as sp
from sympy.abc import x

f_missA = np.poly1d([a_missA, b_missA, c_missA])
f_missB = np.poly1d([a_missB, b_missB, c_missB])
f_missC = np.poly1d([a_missC, b_missC, c_missC])
f_missD = np.poly1d([a_missD, b_missD, c_missD])

x_A1, x_A2  = sp.solve(sp.Eq(f_missA(x), 300), x) # Solving for the 2 x-values where the height of
x_B1, x_B2  = sp.solve(sp.Eq(f_missB(x), 300), x) # missiles above sea is 300m. Since we are finding where they
x_C1, x_C2  = sp.solve(sp.Eq(f_missC(x), 300), x) # land, only the 2nd value of the 2 solutions will be considered.
x_D1, x_D2  = sp.solve(sp.Eq(f_missD(x), 300), x) # i.e. only x_A2, x_B2... etc. will be considered.

strike_coords_A = (x_A2, f_missA(x_A2))
strike_coords_B = (x_B2, f_missB(x_B2))
strike_coords_C = (x_C2, f_missC(x_C2))
strike_coords_D = (x_D2, f_missD(x_D2))

print(strike_coords_A)
print(strike_coords_B)
print(strike_coords_C)
print(strike_coords_D)


# In[5]:


xO_A1, xO_A2  = sp.solve(sp.Eq(f_missA(x), 0), x) # Solving for the 2 x-values where the height of
xO_B1, xO_B2  = sp.solve(sp.Eq(f_missB(x), 0), x) # missiles above sea is 0m. Since we are finding where they originated
xO_C1, xO_C2  = sp.solve(sp.Eq(f_missC(x), 0), x) # from, only the 1st value of the 2 solutions will be considered.
xO_D1, xO_D2  = sp.solve(sp.Eq(f_missD(x), 0), x) # i.e. only xO_A1, xO_B1... etc. will be considered.

orig_coords_A = (xO_A1, f_missA(xO_A1))
orig_coords_B = (xO_B1, f_missB(xO_B1))
orig_coords_C = (xO_C1, f_missC(xO_C1))
orig_coords_D = (xO_D1, f_missD(xO_D1))

print(orig_coords_A)
print(orig_coords_B)
print(orig_coords_C)
print(orig_coords_D)

