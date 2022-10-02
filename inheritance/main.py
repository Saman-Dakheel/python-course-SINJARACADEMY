# class Library:
#     # constructor
#     def __init__(self , library_name , type , book_numbers ):
#         self.book_numbers = book_numbers
#         self.type = type
#         self.library_name = library_name
#     def open(self):
#         print(f'{self.library_name} open and  have {self.book_numbers} of books')
#     def types(self):
#         for i in self.type:
#             print(i)
#
# type = ['lover_books', 'motivation', 'science']
# lib1 = Library(library_name='shingal', type=type, book_numbers=90 )
# lib1.open()
# lib1.types()


# Base Class = Parent Class
class Parent:
    def __init__(self):
        print("Parent Constructor Called ")
    def parent_method(self):
        print('Parent function from parent class')
    def parent_method1(self):
        print('Parent function from parent class')
    def parent_method2(self):
        print('Parent function from parent class')
# Derived Class = Child Class
class Child(Parent):
    def __init__(self):
        print("Child Constructor Called ")
    def child_method(self):
        print('Child function from parent class')

ch = Child()
ch.parent_method()
ch.child_method()
