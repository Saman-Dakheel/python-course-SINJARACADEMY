# def fullName(firstName, lastName , SurName, age):
#     print(
#         "Your Full name {} {} {} , age is {}"
#         .format(lastName ,firstName,SurName , age))
# while True:
#     fName = input('Enter First Name: ')
#     sName = input('Enter Second Name: ')
#     surName = input('Enter surName: ')
#     a = int(input("Enter age : "))
#     fullName(fName, sName , surName , a)


# def nazi(num1, num2):
#     result = num1 + num2
#     print(result)
# def lawand(num1 , num2):
#     result = num1 - num2
#     print(result)
# lawand(9,4)
# nazi(3,8)


# def animal(*any):
#     for i in range(len(any)):
#             print(f"Animal Name {any[i]}")
# animal('Cat', 'mouse' , 'lion', 'hourse')
# animal('Cat' , 'lion', 'hourse')


#
# def animal(**any):
#     print(f"Animal Name {any['lname']}")
#     print(f"Animal Name {any['fname']}")
# animal(fname = 'tom' ,lname = 'jerry' )


# def welcome(name):
#     print(f"Welcome To Sinjar academy {name}")
#
# welcome("bahzany")


# def welcome(name):
#     print(f"Welcome To Sinjar academy {name}")
#
# n = input('Enter your name: ')
# welcome(n)
# welcome("farhad")

# def multiply(num1, num2):
#     result = num1 * num2
#     print(result)
# multiply(3,6)

#
#
# def multiply(*number):
#     result = 1
#     for i in range(len(number)):
#         result = result * number[i]
#     print(result)
#     multiply(3,6 , 2)


# def najya(*name):
#     for i in range(len(name)):
#         if i == 3:
#             print(f"Welcome to here Mrs. {name[i]}")
#         else:
#             print("Your index is not valid")
# najya("Najya" , 'Dler' , "Ghada", "lava")

# def myFunction(**name):
#     print(f"your name is {name['n']}")
#     print(f"your name is {name['f']}")
#     print(f"your name is {name['b']}")
#     print(f"your name is {name['l']}")
# myFunction( n = 'Marwan' ,
#             f = 'farhad',
#             b = 'bahzani' ,
#             l = 'lava')

# def carname(name  = 'Alentra'):
#     print("Car name is {}".format(name))
#
# carname('toyota')
# carname()

# def numbers(myList):
#     for i in range(len(myList)):
#         print(myList[i])
# list1 = [ 1,2 ,3,4,5 ]
# numbers(list1)
# for i in list1:
#     print(i)


# def sub(num1 , num2):
#    return num1 - num2
# print(sub(6,3))

# def sub(num1, num2):
#     result = num1 - num2
#     return result
#
# result = sub(9, 3)
# result =result + 4
# result *= 3
# print(result)


# def ameer():
#     pass
# print('where are you ameer')
# ameer()


# question


# def recursion(k):
#     if (k > 0):
#         result = k + recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# recursion(8)


# def rec():
#     print("Welcome")
#     rec()
#
# rec()

# factorial 3
# 1 * 2 * 3
# import second

# from second import factorial , sub
# print(factorial(5))
# print(sub(8,3))

# import second
# print(second.factorial(4))
# print(second.sub(9,1))
#
#
#
# import second as s
# print(s.factorial(4))
# print(s.sub(9,1))

# import second as s
# print(s.sub(9,1))
# print(s.add(9,1))


#
# def zakria(name= 'zakria'):
#     print('your name is {}'.format(name))
# zakria('saman')

# def funclist(mylist):
#     for i in range(len(mylist)):
#         print(mylist[i])
# list1 = [1,2,7,0,9]
# funclist(list1)


#
# def funclist(mylist):
#     for i in mylist:
#         print(i)
# list1 = [1,2,7,0,9]
# funclist(list1)


# def sum(num1 , num2):
#     result=num1 + num2
#     return  result
#
# result = sum(7,9)
# result *= 7
# print(result)

#
# def doSomething():
#     pass
# print('saman')
# doSomething()


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
# tri_recursion(6)

# factorial 5
# 1 * 2 * 3 * 4 * 5

# def factorial(num):
#     if num == 1 :
#         return 1
#     else:
#         return (num * factorial(num - 1))
# print(factorial(3))


# import third as t
# print(t.factorial(5))
# print(t.sub(9,3))


# import third
# print(third.factorial(5))
# print(third.sub(9,3))


#
# from third import factorial
# print(factorial(5))


# from datetime import date # package
# def calculateAge(birthdate):
#     today = date.today()
#     print(today)
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age
# print(calculateAge(1997, 1,1)+"year")


# x=50
# arrya=[30,64,77,81,99,32,57,31]
# if x>64 :
#     print("yes")
# else:
#     print("no")
# if x > 30 :
#     print("yes")
# else:
#      print("no")


# from datetime import date
# def calculateAge(born):
#     today = date.today()
#     print(today)
#     try:
#         birthday = born.replace(year=today.year)
#
#     except ValueError:
#         birthday = born.replace(year=today.year,
#                                 month=born.month + 1, day=1)
#
#     if birthday > today:
#         return today.year - born.year - 1
#     else:
#         return today.year - born.year
#
# print(calculateAge(date(1997, 2, 3)), "years")


# def goto():
#     for i in range(1, 4):
#         for j in range(1, 4):
#             for k in range(1, 4):
#                print(j, i * k, k)
#                if k == 3:
#                    return None
#
# goto()
# print("did a break from a nested for loop")
