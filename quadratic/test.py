import os 

class Q:
    input = {"a":0, "b":0 , "c":0}
    output = {"x1":0, "x2":0}
    def __init__(self,input,output):
        self.input = input
        self.output = output

    def printResult(self):
        return self.input

IN = {"a": 10, "b": 20, "c": 30}
OUT = {"x1":10, "x2":20}
in1 = Q(IN,OUT)
print(in1.printResult())
# result = in1.printResult
# print(result)
in1.printResult

# class test:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b

#     def testp(self,a,b):
#         return a + b

# b = test(1,2)

# print(b.testp(1,2))

# class MyClass:
# 	"This is my second class."
# 	a = 10
# 	def func(self):
# 		print('Hello')

# # Output: 10
# print(MyClass.a)

# # Output: <function MyClass.func at 0x0000000003079BF8>
# print(MyClass.func)

# # Output: 'This is my second class'
# print(MyClass.__doc__)

# Name = input("Please enter your name?") vscode output cant take input.



# import numpy
# import matplotlib
# from matplotlib import pyplot
# # %matplotlib inline
# x=numpy.linspace(0,3);
# y=x;
# pyplot.plot(x,y);
# y=x+2;
# pyplot.plot(x,y);
# y=x-3;
# pyplot.plot(x,y);
# pyplot.title("Equations of the form y=mx+b")
# pyplot.xlabel("x axis")
# pyplot.ylabel("y axis");
# #pyplot.legend("y=x","y=x+2","y=x-3");
# print ('y=mx+b');
# #m is constant, b is fixed distance. (x,y) vary for different points on the line 
# pyplot.grid()
# pyplot.show()


# from sympy import Symbol, plot
# x = Symbol('x')
# # plot(5*x+2)

# a = plot(-2*x+2,-x**2+2*x+3,(x,-5,5), xlim=[-3,3], ylim=[0,7], legend = True , show = False)
# a[0].line_color = "b"
# a[1].line_color = "r"
# a.show()

# from sympy import plot_implicit, cos, sin, symbols, Eq, And
# x, y = symbols('x y')
# # p5 = plot_implicit(Eq(x**2 + y**2, 5),(x, -5, 5), (y, -2, 2),adaptive=False, points=400)
# p8 = plot_implicit(-2*x+2,-x**2+2*x+3,y - 2, y_var=y)

from sympy import plot_implicit, cos, sin, symbols, Eq, And
x, y = symbols('x y')
# p5 = plot_implicit(Eq(x**2 + y**2, 5),(x, -5, 5), (y, -2, 2),adaptive=False, points=400)
p8 = plot_implicit(-x**2+2*x+3)

# # 3d graph
# from sympy import symbols
# from sympy.plotting import plot3d

# x, y = symbols('x y')
# # Run code block in SymPy Live
# plot3d(x*y, (x, -5, 5), (y, -5, 5))
