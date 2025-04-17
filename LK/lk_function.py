def add_numbers(num1, num2):
    sum = num1 + num2
#    print(sum)
number1 = 5
number2 = 10

add_numbers(3,4)
add_numbers("abc","def")

add_numbers(number1, number2)

add_numbers(num2=7,num1=4)

def var_args(*args):
    sun = 0
    for i in args:
        sun+=i
    return sun, "ok"



print(var_args(1,2,3))
var_args(1,2,3,4,5,6)

message = 'Hello'
def greet():
    global message
#    print('Local', message)
    message = 'xsdd'
greet()

#result = var_args(1,2,3,4,5,6)


result = lambda a,b:print(a+b)
a = 3
b = 4
result (a,b)
