# # encapsulation
# class Person:
#     def __init__(self , name ,age,hieght , gender  ):
#         self._name = name
#         self._age = age
#         self.hieght = hieght
#         self.gender = gender
#     def set_name(self , name):
#         self._name = name
#     def get_name(self ):
#         return self._name
#     def display_person(self):
#         print(f'{self._name} , {self._age}')
# class Shaker(Person):
#     def __init__(self):
#         pass
#     def print_shkaer(self , name , age):
#         self._name = name
#         self._age = age
#
# person = Person(name= 'saman dakheel', age=13, hieght=178,gender= 'male')
# person.display_person()
# person.set_name('Nazi Qolo')
# person.display_person()
# print(person.get_name())
# person.set_name('Imad')
# person.display_person()
#
# shaker =Shaker()
# shaker.print_shkaer(name= ' Shaker' , age=199)
# shaker.display_person()



class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()