
# from math import sqrt

# def quadratic(a,b,c):
#     neg_b = b*-1;
#     b_sq = pow(b,2)
#     a2 = 2*a
#     ac4 = a*c*4
#     b_sqminusac4 = b_sq-ac4
#     axisSymmetry = neg_b/a2
    
#     if (b_sqminusac4)>=0:
#         x1 = (neg_b+(sqrt(b_sqminusac4)))/a2
#         x2 = (neg_b-(sqrt(b_sqminusac4)))/a2
#         return {"x1":x1, "x2":x2, "i1":0, "i2":0}
#     if (b_sqminusac4)<=0:
#         modulas = (b_sqminusac4)*-1
#         IM = (sqrt(modulas))/a2
#         RE = neg_b/a2
#         return {"x1":RE, "x2":RE, "i1":IM, "i2":IM*-1}
#     else:
#         return {"x1":0, "x2":0, "i1":0, "i2":0}


# if __name__ == "__main__":
#     a=[1,1,1]
#     b=[6,-2,-3]
#     c=[5,1,10]
#     print(quadratic(a[0],b[0],c[0]))
#     # output : {'x1': -1.0, 'x2': -5.0, 'i1': 0, 'i2': 0}
#     print(quadratic(a[1],b[1],c[1]))
#     # output : {'x1': 1.0, 'x2': 1.0, 'i1': 0, 'i2': 0}
#     print(quadratic(a[2],b[2],c[2]))
#     # output : {'x1': 1.5, 'x2': 1.5, 
#     #         'i1': 2.7838821814150108, 
#     #         'i2': -2.7838821814150108}
#     print(quadratic(a[2],b[2],0))
#     # output :{'x1': 3.0, 'x2': 0.0, 'i1': 0, 'i2': 0}


from math import sqrt
from sympy import Symbol, plot

class Quadratic:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def find_roots(self):
        neg_b = self.b*-1;
        b_sq = pow(self.b,2)
        a2 = 2*self.a
        ac4 = self.a*self.c*4
        b_sqminusac4 = b_sq-ac4
        axisSymmetry = neg_b/a2
        
        if (b_sqminusac4)>=0:
            x1 = (neg_b+(sqrt(b_sqminusac4)))/a2
            x2 = (neg_b-(sqrt(b_sqminusac4)))/a2
            return {"x1":x1, "x2":x2, "i1":0, "i2":0}
        if (b_sqminusac4)<=0:
            modulas = (b_sqminusac4)*-1
            IM = (sqrt(modulas))/a2
            RE = neg_b/a2
            return {"x1":RE, "x2":RE, "i1":IM, "i2":IM*-1}
        else:
            return {"x1":0, "x2":0, "i1":0, "i2":0}

    def plot_graph(self):
        x = Symbol('x')
        a = plot(self.a*x**2+self.b*x+self.c, legend = True , show = False)
        a[0].line_color = "b"
        # a[1].line_color = "r"
        a.show()

if __name__ == "__main__":
    a=[1,1,1]
    b=[6,-2,-3]
    c=[5,1,10]
    
    q1 = Quadratic(1,6,5)
    print(q1.find_roots())
    q1.plot_graph()