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