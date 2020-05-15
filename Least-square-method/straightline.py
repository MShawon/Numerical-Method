from tabulate import tabulate
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
