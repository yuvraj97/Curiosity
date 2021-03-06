# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:54:12 2019

@author: Yuvraj
"""

import MultiVariable as mvar

# Step1: define a function example f(x,y) = x^y + y^4 + x^2*y + x^3*y + xy
def f(X,Y):
    return X**4 + Y**4 + (X**2)*Y + Y*(X**3) + X*Y

# If you want to usr sins, cosines, tanh, exp, log, .......
# So you must use those functions using numpy as shown:
'''
import numpy as np
def f(X, Y):
    return np.sin(X)*X + np.cos(Y)*Y
'''

# Step2: set variables as shown
x_axis, y_axis,  dx, dy = (-10,10) ,(-10,10) ,0.5 ,0.5
m = mvar.MultiVariable(f, x_axis, dx, y_axis, dy)
# Here the arguments are as follow
# Arg1: function that you defined in Step1
# Arg2: The range of X axes
# Arg3: dx i.e. difference b/w two adjacent x's
# Arg4: The range of Y axes
# Arg5: dy i.e. difference b/w two adjacent y's

# To plot the function
m.plot_surface_color_3D()

''' To plot slice of a function: '''
# 1: along X axis given value of x: x_value
m.plot_function_wrtX(x_value=5, plot_2D_or_3D='3d', plot_separately=True)   # to plot 3D
    #(it might seem useless to draw a 3D plot of a 2D plot but it might be usefull to visualize graph and derivatice more clearly)
m.plot_function_wrtX(x_value=5, plot_2D_or_3D='2d', plot_separately=True)   # to plot 2D
# 2: along Y axis given value of y: y_value
m.plot_function_wrtY(y_value=5, plot_2D_or_3D='3d', plot_separately=True)   # to plot 3D
m.plot_function_wrtY(y_value=5, plot_2D_or_3D='2d', plot_separately=True)   # to plot 2D

''' To plot the nth derivative of function with respect to X '''
m.plot_diff_wrtX(order_of_diff=1)       # D_x
m.plot_diff_wrtX(order_of_diff=1)       # D_xx

''' To plot the nth derivative of function with respect to Y '''
m.plot_diff_wrtY(order_of_diff=1)       # D_y
m.plot_diff_wrtY(order_of_diff=1)       # D_yy

''' To plot 3D nth derivative of function with respect to X give value of Y = y_value '''
m.plot_diff_wrtX_given_Y(y_value=5, order_of_diff=1, plot_2D_or_3D='3d', plot_separately=True)
''' To plot 2D nth derivative of function with respect to X give value of Y = y_value '''
m.plot_diff_wrtX_given_Y(y_value=5, order_of_diff=1, plot_2D_or_3D='2d', plot_separately=True)


''' To plot #D nth derivative of function with respect to X give value of Y = y_value'''
m.plot_diff_wrtY_given_X(x_value=5, order_of_diff=1, plot_2D_or_3D='3d', plot_separately=True)
''' To plot #D nth derivative of function with respect to X give value of Y = y_value '''
m.plot_diff_wrtY_given_X(x_value=5, order_of_diff=1, plot_2D_or_3D='2d', plot_separately=True)

''' This method will be very handy
    like you wanna plot the partial derivatives like:
        D_x, D_xx, D_xxx, D_xyx, D_xxy, D_xyy, D_yxy, D_xxxy, D_xyxx, D_xyyy ..........
    So you can do it using this method (of class 'MultiVariable':  
    plot_diff_of_sequence(sequence)
    Argument:
        sequence: it is a sting of x's and y's thst defines the order of partial derivatives like:
            'xxyx' mean D_xxyx
            'xyyy' mean D_xyyy
'''
m.plot_diff_of_sequence('xy')       # plot partial derivative D_xxx
# m.plot_diff_of_sequence('xxx')      # plot partial derivative D_xxx
# m.plot_diff_of_sequence('xyxy')     # plot partial derivative D_xxx
# m.plot_diff_of_sequence('xyyy')     # plot partial derivative D_xxx

''' To set limits on axis's '''
# m.setZ_limit((-5,5))     # To set limit on Z axis
# m.setY_limit((-5,5))     # To set limit on Y axis
# m.setX_limit((-5,5))     # To set limit on X axis
# m.set_axes_limit((-5,5)) # To set limit on X, Y and Z axis simentaneouslt


# ===============================================================================
# Plotting piecewise function
# Say you wanna implement function
#   f(X,Y) =   X^2 + Y^2 ; -5 <= X <0
#              X^2 - Y^2 ;  0 <= X <=5

def f(X,Y):
    import numpy as np
    Z = np.zeros(X.shape)
    Z += ((X >=-10) & (X < 0))*(X**2 + Y**2) # X^2 + Y^2 ; -5 <= X <0
    Z += ((X >= 0) & (X <=10))*(X**2 - Y**2) # X^2 - Y^2 ;  0 <= X <=5
    return Z

m = mvar.MultiVariable(f, x_axis, dx, y_axis, dy)

m.plot_surface_color_3D()