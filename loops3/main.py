# password ="python"
# counter = 0
# while True:
#     user_input = input("Enter your password: ").lower()
#     counter += 1
#     if user_input == password:
#         break  # true        and   false
#     elif user_input != password and counter > 2:
#         print("your password incorrect")
#         break
#     else:
#         print("your password incorrect try again")


# cars = ['BMW', 'MARCEDS', 'FAW']
# for saad in cars:
#     if saad == 'MARCEDS':
#         continue
#     print(saad)

# cars = ['BMW', 'MARCEDS', 'FAW']
# for saad in cars:
#     print(saad)
#     if saad == 'MARCEDS':
#         continue

# for i in range(200):
#     pass
#     print(i)

# for i in range(200):
#     print(i)
#     pass


# for i in range(200):
#     if i < 10:
#         continue
#     else:
#         print('shaha {}'.format(i))


# view = ['big','medium','small']
# fruits = ['apple' , 'orange', 'banana']
# for i in view:
#     for j in fruits:
#         print(i, j)



# view = ['big','medium','small']
# fruits = ['apple' , 'orange', 'banana']
# for i in view:
#     for j in fruits:
#         print(i,end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()
