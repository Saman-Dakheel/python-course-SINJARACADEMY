def factorial(num):

    if num == 1 :
        return 1
    else:
        return (num * factorial(num - 1))


global result
def sub(num1, num2):
    result = num1 - num2
    return  result
def add(num1, num2):
    result = num1 + num2
    return result
result  = sub(5,4)
print(result + 9)
