import math

def quadratic(a,b,c):
    tempb1 = b*-1;
    tempb2 = pow(b,2)
    tempa = 2*a
    befSqr = a*c*4
    if (tempb2-befSqr)>=0:
        x1 = (tempb1+(math.sqrt(tempb2-befSqr)))/tempa
        x2 = (tempb1-(math.sqrt(tempb2-befSqr)))/tempa
        i1 = 0
        i2 = 0
        return {"x1":x1, "x2":x2, "i1":i1, "i2":i2}
    if (tempb2-befSqr)<=0:
        modulas = (tempb2 - befSqr)*-1
        IM = (math.sqrt(modulas))/tempa
        RE = tempb1/tempa
        x1 = RE
        x2 = RE
        i1 = IM
        i2 = IM*-1
        return {"x1":x1, "x2":x2, "i1":i1, "i2":i2}
    else:
        return {"x1":0, "x2":0, "i1":0, "i2":0}


if __name__ == "__main__":
    a=[1,1,1]
    b=[6,-2,-3]
    c=[5,1,10]
    print(quadratic(a[0],b[0],c[0]))
    # output : {'x1': -1.0, 'x2': -5.0, 'i1': 0, 'i2': 0}
    print(quadratic(a[1],b[1],c[1]))
    # output : {'x1': 1.0, 'x2': 1.0, 'i1': 0, 'i2': 0}
    print(quadratic(a[2],b[2],c[2]))
    # output : {'x1': 1.5, 'x2': 1.5, 
    #         'i1': 2.7838821814150108, 
    #         'i2': -2.7838821814150108}
   
