# polymorphism

# class Human:
#     def __init__(self,name):
#         self.name =name
#     def display(self):
#         print(f'Human name : {self.name}')
# class Male(Human):
#     def __init__(self , wieght ):
#         self.wieght = wieght
#     def display(self):
#         print(f'Male wieght is {self.wieght}')
# h = Human(name='saman')
# h.display()
# m = Male(wieght=90)
# m.display()


#
# from fly import Penguin
#
# peggy = Penguin()
# peggy.fly()









# polymarphism تعدد الاشكال يعني نفس الاسم ب وضائف مختلفة

# class Human :
#     def display(self , name):
#         print(f'This is Human Class {name}')
# class Person(Human):
#     def display(self , gender):
#         print(f'This person class you are {gender}')
#
# m =Person()
# m.display(gender='male')



class Parrot:
    def fly(self):
        print("Parrot can fly")
class Penguin(Parrot):
    def fly(self):
        print("Penguin can't fly")
blu=Parrot()
peggy = Penguin()
blu.fly()
peggy.fly()














