# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:42:52 2023

@author: grover.laporte
Nonlinear optmization demonstration in a 1D solution space
Demo1: Bisection method for finding a zero

"""
import numpy as np
import pandas as pd
import plotly.express as px


import streamlit as st
st.write("""
          # Bisection Method Demonstration
          Given the function $3x^2-12$ whose zeros lie at -2,2; watch the algorithm get
          close to the solution by taking incremental steps.
          """)



def bisection_step(f,a,b,TOL=1E-4):
    """
    bisection - an algorithm to find a zero of a function.
        Condition: initially f(a) and f(b) must have 
        different signs.
    Input:  f - the function to find the root
            a - left limit to start the algorithm
            b - right limit to start the algorithm
    
    Output: a,b which is the next step of the algorithm for visual purpose.
    
    """
    if f(a)*f(b)>0:
        return "Endpoints must have opposite signs."
    p = (a+b)/2
    if f(a)*f(p) < 0:
        b=p
    else:
        a=p
    return a,b

f = lambda x: 3*x**2-12
a = 0
b = 5
max_step = 5
a_list = [a];b_list = [b]
t = np.linspace(-5,5,100)
for step in range(max_step):
    a,b = bisection_step(f,a,b)
    a_list.append(a)
    b_list.append(b)
          
idx = st.number_input(":blue[**Choose a step**]",min_value=0,max_value=4,
                      step=1)

curr_val = (a_list[idx]+b_list[idx])/2
st.write("#### Current estimated value = "+str(curr_val))
st.write("#### $f(x) = 3x^2-12$")
fig = px.line(x=t,y=f(t),color_discrete_sequence=["black"])
fig.add_scatter(x=[a_list[idx],b_list[idx]],y=[0,0],name = "a / b")
fig.add_scatter(x=[curr_val],y=[0],
                marker=dict(symbol="x",color="salmon",size=10),
                name = "Estimate")
st.plotly_chart(fig)


