welcome="""
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
#*                                                                   #*
#*                        Curve Fitting                              #*
#*                              By                                   #*
#*                     Least Square Method                           #*
#*         Find the Parabola that BEST fits for your data            #*
#*                     Credit- Monirul Shawon                        #*
#*                                                                   #*
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
"""
print(welcome)

import numpy as np
from tabulate import tabulate
curve="""
 {1} Y = aX^2 + bX + c
 {2} Y = a + bX + cX^2
"""
print(curve)
choice=input("1 or 2 ? : ")

def Parabola1():
    try:
        x=[]
        y=[]
        n=int(input("How many number of sets you've got there? \n n= "))
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
        #x^2
        squarex=[a*a for a in x]
        #x^3
        cubex=[a*a*a for a in x]
        #x^4
        quadx=[a*a*a*a for a in x]
        #making x*y row
        multi=[a*b for a,b in zip(x,y)]
        #x*x*y
        xsquarey=[a*b for a,b in zip(x,multi)]
        #table
        table=[(p,q,r,s,t,u,v) for p,q,r,s,t,u,v in zip(x,y,squarex,cubex,quadx,multi,xsquarey)]
        headers=['x','y','x^2','x^3','x^4','xy','x^2*y']
        print(tabulate(table,headers,tablefmt="pretty"))
        #table summation
        sumx=sum(x)
        sumy=sum(y)
        sumsquarex=sum(squarex)
        sumcubex=sum(cubex)
        sumquadx=sum(quadx)
        sumxy=sum(multi)
        sumxsquarey=sum(xsquarey)
        #table2
        table2=[(sumx,sumy,sumsquarex,sumcubex,sumquadx,sumxy,sumxsquarey)]
        headers2=['∑x','∑y','∑x^2','∑x^3','∑x^4','∑xy','∑x^2*y']
        print(tabulate(table2,headers2,tablefmt="pretty"))

        print(f"\nEquation 1 is: {sumy} = {sumsquarex} a + {sumx} b + {n} c")
        print(f"Equation 2 is: {sumxy} = {sumcubex} a + {sumsquarex} b + {sumx} c")
        print(f"Equation 3 is: {sumxsquarey} = {sumquadx} a + {sumcubex} b + {sumsquarex} c")
        #calculation
        A=np.array([[sumsquarex,sumx,n],[sumcubex,sumsquarex,sumx],[sumquadx,sumcubex,sumsquarex]])
        B=np.array([sumy,sumxy,sumxsquarey])
        X=np.linalg.solve(A,B)
        print("So, the best fitted Parabola for your data is:")
        if X[2]<0:
            print(f" Y = {X[0]} X^2 + {X[1]} X {X[2]}")
        elif X[1]<0:
            print(f" Y = {X[0]} X^2 {X[1]} X + {X[2]}")
        else:
            print(f" Y = {X[0]} X^2 + {X[1]} X + {X[2]}")
    except:
        print("\nPlease input number to continue your calculation")

def Parabola2():
    try:
        x=[]
        y=[]
        n=int(input("How many number of sets you've got there? \n n= "))
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
        #x^2
        squarex=[a*a for a in x]
        #x^3
        cubex=[a*a*a for a in x]
        #x^4
        quadx=[a*a*a*a for a in x]
        #making x*y row
        multi=[a*b for a,b in zip(x,y)]
        #x*x*y
        xsquarey=[a*b for a,b in zip(x,multi)]
        #table
        table=[(p,q,r,s,t,u,v) for p,q,r,s,t,u,v in zip(x,y,squarex,cubex,quadx,multi,xsquarey)]
        headers=['x','y','x^2','x^3','x^4','xy','x^2*y']
        print(tabulate(table,headers,tablefmt="pretty"))
        #table summation
        sumx=sum(x)
        sumy=sum(y)
        sumsquarex=sum(squarex)
        sumcubex=sum(cubex)
        sumquadx=sum(quadx)
        sumxy=sum(multi)
        sumxsquarey=sum(xsquarey)
        #table2
        table2=[(sumx,sumy,sumsquarex,sumcubex,sumquadx,sumxy,sumxsquarey)]
        headers2=['∑x','∑y','∑x^2','∑x^3','∑x^4','∑xy','∑x^2*y']
        print(tabulate(table2,headers2,tablefmt="pretty"))

        print(f"\nEquation 1 is: {sumy} = {n} a + {sumx} b + {sumsquarex} c")
        print(f"Equation 2 is: {sumxy} = {sumx} a + {sumsquarex} b + {sumcubex} c")
        print(f"Equation 3 is: {sumxsquarey} = {sumsquarex} a + {sumcubex} b + {sumquadx} c")
        #calculation
        A=np.array([[sumsquarex,sumx,n],[sumcubex,sumsquarex,sumx],[sumquadx,sumcubex,sumsquarex]])
        B=np.array([sumy,sumxy,sumxsquarey])
        X=np.linalg.solve(A,B)
        print("So, the best fitted Parabola for your data is:")
        if X[0]<0:
            print(f" Y = {X[2]} + {X[1]} X {X[0]} X^2")
        elif X[1]<0:
            print(f" Y = {X[2]} {X[1]} X + {X[0]} X^2")
        else:
            print(f" Y = {X[2]} + {X[1]} X + {X[0]} X^2")
    except:
        print("\nPlease input number to continue your calculation")

if choice=='1':
    Parabola1()
elif choice=='2':
    Parabola2()
else:
    print("Your didn't chose a valid number")
