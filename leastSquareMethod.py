#welcome screen
print("-"*72)
print("""+                           Least Square Method                        +
+  The least square method is the process of finding the best-fitting  +
+  curve or line of best fit for a set of data points by reducing the  +
+  sum of the squares of the offsets (residual part) of the points     +
+  from the curve.                                                     +""")
print("-"*72)
#########################################################################
#animation
import time
import sys
print("Wait a sec")
animation = "|/-\\"
for i in range(60):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print ("\nProgram Loaded Succesfully!")
########################################################################
import numpy as np
import math
from tabulate import tabulate
#clearscreen
def clear_screen():
    import os
    os.system("clear") # Linux - OSX
    os.system("cls") # Windows
#welcometext
welcometext="""
{+}-----------------------{+}---------------------------{+}
 #                                                       #
 #          1) Straight line: y=ax+b                     #
 #          2) Parabola: y=ax^2+bx+c or y=a+bx+cx^2      #
 #          3) Exponential curve: y=ae^bx                #
 #          4) Curve: y=ax^b and                         #
 #          5) Another curve: y=ab^x                     #
 #        {99} Exit                                      #
 #                                                       #
{+}-----------------------{+}---------------------------{+}
"""
print("\nFollowing are the available option for Curve fitting:")
print(welcometext)
print("To Use any of the curve input corresponding number:")
#######################################################################
while True:
    try:
        curve=input("\nSelect a Curve= ")
        clear_screen()
        #straight line
        if curve=='1':
            welcome="""
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            #*                                                                   #*
            #*                        Curve Fitting                              #*
            #*                              By                                   #*
            #*                     Least Square Method                           #*
            #*       Find the Straight Line that BEST fits for your data         #*
            #*                     Credit- Monirul Shawon                        #*
            #*                                                                   #*
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            """
            print(welcome)
            x=[]
            y=[]
            try:
                n=int(input("How many number of sets you've got there? \n n= "))
                print("Let, Y=mX+c")
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
                #making x square row
                squarex=[a*a for a in x]
                #making x*y row
                multi=[a*b for a,b in zip(x,y)]
                #table
                table=[(p,q,r,s) for p,q,r,s in zip(x,y,squarex,multi)]
                headers=['x','y','x^2','xy']
                print(tabulate(table,headers,tablefmt="pretty"))
                #table summation
                sumx=sum(x)
                sumy=sum(y)
                sumsquarex=sum(squarex)
                sumxy=sum(multi)
                #table2
                table2=[(sumx,sumy,sumsquarex,sumxy)]
                headers2=['∑x','∑y','∑x^2','∑xy']
                print(tabulate(table2,headers2,tablefmt="pretty"))
                #print equation
                print(f"\nEquation 1 is: {sumx} a + {n} b = {sumy}")
                print(f"Equation 2 is: {sumsquarex} a + {sumx} b = {sumxy}")
                #calculation
                p=float(((sumy*sumx)-(sumxy*n)))
                q=float(((sumxy*sumx)-(sumy*sumsquarex)))
                r=float(((sumx*sumx)-(n*sumsquarex)))
                a=float(p/r)
                b=float(q/r)
                if b>0:
                    print("\nThe Best fitted Straight Line for your data is Y = {} X + {}".format(a,b))
                else:
                    print("\nThe Best fitted Straight Line for your data is Y = {} X {}".format(a,b))
            except:
                print("\nNo.. input is not a number. It's a string.")
                print("Please input number to continue your calculation")

        #Parabola
        elif curve=='2':
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
                    #print equation
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
                    #print equation
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
            #choice a curve
            if choice=='1':
                Parabola1()
            elif choice=='2':
                Parabola2()
            else:
                print("You didn't choose a valid number")
        #exponential curve
        elif curve=='3':
            welcome="""
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            #*                                                                   #*
            #*                        Curve Fitting                              #*
            #*                              By                                   #*
            #*                     Least Square Method                           #*
            #*       Find the Exponential Curve that BEST fits for your data     #*
            #*                     Credit- Monirul Shawon                        #*
            #*                                                                   #*
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            """
            print(welcome)
            x=[]
            y=[]
            try:
                n=int(input("How many number of sets you've got there? \n n= "))
                print('-'*70)
                print("Let, y=ae^(bx) or Y=A+Bx where Y=log10(y) , A=log10(a) and B=blog10(e) ")
                print('-'*70)
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
                #making x square row
                squarex=[a*a for a in x]
                #making Y=log10(y) row
                Y=[math.log10(b) for b in y]
                #making x*y row
                multi=[a*b for a,b in zip(x,Y)]
                #table
                table=[(p,q,r,s,t) for p,q,r,s,t in zip(x,y,Y,squarex,multi)]
                headers=['x','y','Y=log10(y)','x^2','xY']
                print(tabulate(table,headers,tablefmt="pretty"))
                #table summation
                sumx=sum(x)
                sumy=sum(y)
                sumY=sum(Y)
                sumsquarex=sum(squarex)
                sumxY=sum(multi)
                #table2
                table2=[(sumx,sumy,sumY,sumsquarex,sumxY)]
                headers2=['∑x','∑y','∑Y','∑x^2','∑xY']
                print(tabulate(table2,headers2,tablefmt="pretty"))
                #print equation
                print(f"\nEquation 1 is: {sumY} = {n} A + {sumx} B")
                print(f"Equation 2 is: {sumxY} = {sumx} A + {sumsquarex} B")
                #solve liner equations
                M=np.array([[n,sumx],[sumx,sumsquarex]])
                N=np.array([sumY,sumxY])
                X=np.linalg.solve(M,N)
                #solve a and b
                a=math.pow(10,X[0])
                b=X[1]/(math.log10(math.e))
                print(f"Hence, the required curve is: y={a} e^({b} x)")
            except:
                print("\nNo.. input is not a number. It's a string.")
                print("Please input number to continue your calculation")
        #curve4
        elif curve=='4':
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
                #print equation
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
        #final curve
        elif curve=='5':
            welcome="""
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            #*                                                                   #*
            #*                        Curve Fitting                              #*
            #*                              By                                   #*
            #*                     Least Square Method                           #*
            #*         Find the y=ab^x Curve that BEST fits for your data        #*
            #*                     Credit- Monirul Shawon                        #*
            #*                                                                   #*
            #*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
            """
            print(welcome)
            x=[]
            y=[]
            try:
                n=int(input("How many number of sets you've got there? \n n= "))
                print("-"*70)
                print("Let, y=ab^x or Y=A+Bx where Y=log10(y) , A=log10(a) and B=log10(b)")
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
                #making x square row
                squarex=[a*a for a in x]
                #making Y=log10(y) row
                Y=[math.log10(b) for b in y]
                #making x*y row
                multi=[a*b for a,b in zip(x,Y)]
                #table
                table=[(p,q,r,s,t) for p,q,r,s,t in zip(x,y,Y,squarex,multi)]
                headers=['x','y','Y=log10(y)','x^2','xY']
                print(tabulate(table,headers,tablefmt="pretty"))
                #table summation
                sumx=sum(x)
                sumy=sum(y)
                sumY=sum(Y)
                sumsquarex=sum(squarex)
                sumxY=sum(multi)
                #table2
                table2=[(sumx,sumy,sumY,sumsquarex,sumxY)]
                headers2=['∑x','∑y','∑Y','∑x^2','∑xY']
                print(tabulate(table2,headers2,tablefmt="pretty"))
                #print equation
                print(f"\nEquation 1 is: {sumY} = {n} A + {sumx} B")
                print(f"Equation 2 is: {sumxY} = {sumx} A + {sumsquarex} B")
                #solve liner equations
                M=np.array([[n,sumx],[sumx,sumsquarex]])
                N=np.array([sumY,sumxY])
                soln=np.linalg.solve(M,N)
                #solve a and b
                a=math.pow(10,soln[0])
                b=math.pow(10,soln[1])
                print(f"Hence, the required curve is: y={a}({b})^x")
            except:
                print("\nNo.. input is not a number. It's a string.")
                print("Please input number to continue your calculation")
        #condition close
        elif curve=='99':
            exit()
        else:
            print("Your Input isn't valid")
            print(welcometext)
            print("\nSelect curve number, i.e, to use straight line input 1")
        #yes or no
        again=str(input("\nWant to calculate again? Yes or No : ")).lower()
        if 'y' in again:
            clear_screen()
            print("Welcome again!")
            print("\nFollowing are the available option for Curve fitting:")
            print(welcometext)
            print("To Use any of the curve input corresponding number:")
            continue
        else:
            exit()
    except:
        print("\nGoodbye!")
        exit()
