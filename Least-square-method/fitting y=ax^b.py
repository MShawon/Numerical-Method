welcome="""
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
#*                                                                   #*
#*                        Curve Fitting                              #*
#*                              By                                   #*
#*                     Least Square Method                           #*
#*         Find the y=ax^b Curve that BEST fits for your data        #*
#*                     Credit- Monirul Shawon                        #*
#*                                                                   #*
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
"""
print(welcome)

import numpy as np
import math
from tabulate import tabulate
x=[]
y=[]
try:
    n=int(input("How many number of sets you've got there? \n n= "))
    print("-"*70)
    print("Let, y=ax^b or Y=A+bX where Y=log10(y) , A=log10(a) and X=log10(x)")
    print("-"*70)
    #taking x values
    print("\nInput values of x: ")
    for i in range(1,n+1):
        xnum=float(input(f" x{i} = "))
        x.append(xnum)
    #taking y values
    print("\nInput values of y:")
    for j in range(1,n+1):
        ynum=float(input(f" y{j} = "))
        y.append(ynum)
    #making X=log10(x)
    X=[math.log10(a) for a in x]
    #making x square row
    squareX=[a*a for a in X]
    #making Y=log10(y) row
    Y=[math.log10(b) for b in y]
    #making x*y row
    multi=[a*b for a,b in zip(X,Y)]
    #table
    table=[(p,q,r,s,t,u) for p,q,r,s,t,u in zip(x,y,X,Y,squareX,multi)]
    headers=['x','y','X=log10(x)','Y=log10(y)','x^2','XY']
    print(tabulate(table,headers,tablefmt="pretty"))
    #table summation
    sumx=sum(x)
    sumy=sum(y)
    sumX=sum(X)
    sumY=sum(Y)
    sumsquareX=sum(squareX)
    sumXY=sum(multi)
    #table2
    table2=[(sumx,sumy,sumX,sumY,sumsquareX,sumXY)]
    headers2=['∑x','∑y','∑X','∑Y','∑x^2','∑XY']
    print(tabulate(table2,headers2,tablefmt="pretty"))

    print(f"\nEquation 1 is: {sumY} = {n} A + {sumX} b")
    print(f"Equation 2 is: {sumXY} = {sumX} A + {sumsquareX} b")
    #solve liner equations
    M=np.array([[n,sumX],[sumX,sumsquareX]])
    N=np.array([sumY,sumXY])
    soln=np.linalg.solve(M,N)
    #solve a and b
    a=math.pow(10,soln[0])
    b=soln[1]
    print(f"Hence, the required curve is: y={a}(x)^{b}")
except:
    print("\nNo.. input is not a number. It's a string.")
    print("Please input number to continue your calculation")
