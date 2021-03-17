def Ln(x):
    temp=1.0
    result=0.0
    minus=-1.0
    if x<0 or x==1.0 :
        return (0.0)
    if ( x>1):
        x=1/x
        temp=temp*(-1.0)
    for i in range (1000):
        p = 1
        for j in range(i+1):
            p=p*(x-1)
        sumer=(p/(i+1))
        minus=-1*minus
        result=(result+minus*sumer)
    return(result*temp)
def exponent(x:float):
    sumer=0
    for i in range(100):
        temp=0
        mona=1
        machna=1
        for j in range(i):
            mona=mona*x
            machna=((j+1)*machna)
        temp=mona/machna
        sumer=sumer+temp
    return (sumer)
def XtimesY(x:float,y:float):
    if x==0.0:
        return(0.0)
    if y==0.0:
        return(1.0)
    if x<0.0 :
        return(0.0)
    if y<0.0:
        y=(-1*y)
        x=(1/x) 
    if y==1.0:
        return(x)
    power=y*Ln(x)
    result=float('%0.6f' %(exponent(power)))
    if result==-0.0:
        result=0.0
    return (result)
def sqrt(x:float,y:float):
    negativ=1.0
    if (x%2!=0) and y<0.0 and x%1==0:## שורש אי זוגי למספר שלילי
      negativ=-1*negativ
      y=y*-1
    if y<0.0 and x%1!=0.0:
        return(0.0)
    if x==0:
        return(0.0)
    x=1/x
    calc=negativ*XtimesY(y,x)
    return(calc)
def calculate(x:float):
#   if x< 0.0:
#        return (0.0)
    calc= float('%0.6f' % (exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)))
    if calc==-0.0:
        calc=0.0
    return(calc)








