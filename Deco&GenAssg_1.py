def multiply(num1, num2):
    print(num1 * num2)

def decor_multiply(func):
    def inner (num1,num2):
        for i in range (2):
            multiply(num1,num2)
        return func(num1,num2)
    return inner

multiply = decor_multiply(multiply)
multiply(2,4)