# class Restaurant:
#     def __init__(self, name, type):
#         self.name = name.title()
#         self.dish = type
#         self.order = 0
#         self.guest = 0
#
#     def open_rest(self):
#         print(f'Welcome {self.name} is  open !!! Come in')
#
#     def services(self):
#         print(f'We serve {self.dish} We hope you liked ')
#
#     def set_order(self, number_of_order):
#         self.order = number_of_order
#
#     def set_guest(self, number_guest):
#         self.guest = number_guest
#
# while True:
#     rest_name = input('Enter Rest Name: ')
#     food_type = input('Enter Food Type: ')
#     rest1 = Restaurant(name = rest_name ,type= food_type)
#     rest1.open_rest()
#     rest1.services()
#     number_of_orders = int(input('Enter Order Number : '))
#     print('Initial Order ' + str(rest1.order))
#     rest1.set_order(number_of_orders)
#     print(' Ordered ' + str(rest1.order))
#     number_of_guest = int(input('Enter Guest Number : '))
#     print('Initial Guest ' + str(rest1.guest))
#     rest1.set_guest(18)
#     print('Your Guest ' + str(rest1.guest))
#
# class User:
#     def __init__(self, name, userName, email, location):
#         self.name = name
#         self.user_name = userName
#         self.email = email
#         self.location = location
#         self.attempts = 0
#
#     def greeting(self):
#         msg = 'Welocme to our Restaurant Application {}'.format(self.name)
#         print(msg)
#
#     def user_info(self):
#         print(f'Name: {self.name}')
#         print(f'User Name: {self.user_name}')
#         print(f'Email : {self.email}')
#         print(f'Location : {self.location}')
#
#     def increment_attempts(self):
#         self.attempts += 1
#
#     def reset_attempts(self):
#         self.attempts = 0
#
#
# user = User(name='Saman',
#             userName='Saman_Dakheel',
#             email='sam@gmail.com',
#             location='Mam Rashan Camp')
#
# user.greeting()
# user.user_info()
# print('Your Attempts {}'.format(user.attempts))
# user.increment_attempts()
# user.increment_attempts()
# user.increment_attempts()
# user.increment_attempts()
# print('Your Attempts {}'.format(user.attempts))
# user.reset_attempts()
# print('Your Attempts {}'.format(user.attempts))


#######################################################################

# class Restaurant:
#     # constructor
#     def __init__(self, name, type):
#         self.name = name.title()
#         self.type = type
#         self.order = 0
#         self.guest = 0
#
#     def open_rest(self):
#         print(f'{self.name} is Opened !!! Come in')
#
#     def rest_food(self):
#         print(f'{self.name} Restaurant serve {self.type} we hope you like')
#
#     def set_order(self, o):
#         self.order = o
#
#     def set_guest(self, g):
#         self.guest = g
#
#
# while True:
#     n = input('Enter Rest Name: ')
#     t = input('Enter Food Type: ')
#     rest = Restaurant(name=n, type=t)
#     rest.open_rest()
#     rest.rest_food()
#     o = int(input('Enter Your Order Number: '))
#     print('Your order : {}'.format(rest.order))
#     rest.set_order(o)
#     print('Your order : {}'.format(rest.order))
#     print('!'*30)
#     g = int(input('Enter Your Guest Number: '))
#     print('Your Guest : {}'.format(rest.guest))
#     rest.set_guest(g)
#     print('Your Guest : {}'.format(rest.guest))


class User:
    def __init__(self, name, user_name, location, email, phone):
        self.name = name
        self.user_name = user_name
        self.location = location
        self.email = email
        self.phone = phone
        self.attempts = 0

    def greeting(self):
        message = f'{self.name} Welcome to our Rest application'
        print(message)

    def user_info(self):
        print(f'Name : {self.name}')
        print(f'User Name : {self.user_name}')
        print(f'Location : {self.location}')
        print(f'Email : {self.email}')
        print(f'Phone Number : {self.phone}')

    def increment_attempts(self):
        self.attempts += 1

    def reset_attempts(self):
        self.attempts = 0


user = User(
    name='Saman',
    user_name='saman_dakheel',
    location='Mam Rashan Camp',
    email='sam@gmail.com',
    phone='07827509472'
)

user.greeting()
user.user_info()
print(f'Your attempts : {user.attempts}')
user.increment_attempts()
user.increment_attempts()
user.increment_attempts()
user.increment_attempts()
user.increment_attempts()
user.increment_attempts()
user.increment_attempts()
print(f'Your attempts : {user.attempts}')
print('#' * 20)
user.reset_attempts()
print(f'Your attempts : {user.attempts}')
