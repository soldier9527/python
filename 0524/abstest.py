def my_abs(x):
    if(x>0):
        return x
    else:
        return -x

def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    
    if(x>0):
        return x
    else:
        return -x
