
# username = 'chaiaurcode'

# def func():
#     username = 'chai'
#     print(username)

# print(username)
# func()


# if we declare a variable globally, we can use under any function, 
# if we declare a new variable same name as globall vaiable and call it under function than it will call the variable which is under function
# if there is no variable for that name then it will call the global variable
# it is like we can talk about our home outside, but we can take outside things to home 


x = 99 
# def func2(y):
#     z = x + y 
#     return z 

# print(func2(5))


# def func3():
#     global x
#     x = 88

# func3()
# print(x)



# def func1():
#     x = 77
#     def func2():
#         print(x)
#     return func2
# myResult = func1()
# myResult()



def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
print(f(3))
g = chaicoder(3)
print(g(3))