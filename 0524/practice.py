import math

def pinstance(arr):
    if not isinstance(arr,list):
        if not isinstance(arr,(int,float)):
            raise TypeError("type is error")
    else:
        for a in arr:
            if not isinstance(a,(int,float)):
                raise TypeError("type is error")
    
def quadratic(a,b,c):
    pinstance(list([a,b,c]))
    if(2*b-4*a*c<0):
        print("do not have answer")
        return 'do not have answer'
    else:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print('ax2+bx+c=0',x1," ",x2)
        return (x1,x2)
quadratic(2,3,1)
quadratic(1,3,-4)