# class Person():
#     welcome = 'Welcome to person class'
#     # create constructor (Attributes)
#     def __init__(self, name, gender, age , hight):
#         # initialize Attributes
#         self.yourName = name
#         self.yourGender = gender
#         self.yourAge = age
#         self.yourHight = hight
#     # methods = Functions
#     def walking(self):
#         print(f'{self.welcome} You are walking {self.yourName}')
#     def drinking(self , type):
#         print(f'you are drinking {type} {self.yourName} ')
#         self.walking()
# # create objects = instance
# person1 = Person('Saman', 'male', 23 ,178)
# print(person1.__class__.welcome)
# print(person1.yourName)
# print(person1.yourGender)
# print(person1.yourAge)
# print(person1.yourHight)
# person1.walking()
# person1.drinking('Coffee')
# print('!'*20)
# person2 = Person(n , 'male' , 30 , 160)
# print(person1.__class__.welcome)
# print(person2.yourName)
# print(person2.yourGender)
# print(person2.yourAge)
# print(person2.yourHight)


class Person():
    welcome = 'Welcome to class person '

    # special method constructor
    def __init__(self, name, gender, age, hight):
        # initialize attributes
        self.yourName = name
        self.yourGender = gender
        self.yourAge = age
        self.yourHight = hight
        self.wieght = 90

    # create methods = functions
    def sleeping(self):
        print('You are sleeping ')

    def language(self, lang):
        print(f"{self.welcome} {self.yourName} You are specking {lang} language")


# create instance = objects
# instance one
person1 = Person('saman', 'male', 23, 178)
print(person1.__class__.welcome)
print(person1.yourName)
print(person1.yourGender)
print(person1.yourAge)
print(person1.yourHight)
print(person1.wieght)
person1.sleeping()
person1.language('kurdish')
print('!'*20)
# instance tow
person2 = Person('Bahzani', 'female' ,30, 160  )
print(person2.__class__.welcome)
print(person2.yourName)
print(person2.yourGender)
print(person2.yourAge)
print(person2.yourHight)
print(person2.wieght)
person2.sleeping()
person2.language('Arabic')