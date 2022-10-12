# f = open(file='file1.txt' , mode='r')
# print(f.readlines())
# print(f.readline())
# print(f.readline())

#
# f = open(file='file1.txt' , mode='r')
# for i in f:
#     print(i)
# f.close()

# f = open(file='C:\\Users\\Saman\\Desktop\\shaha.txt' , mode='r')
# print(f.readline())



# f = open('file2.txt', 'a')
# f.write('We are dialing with files ')
# f.close()
#
# f = open('file2.txt' , 'r')
# print(f.readline())


# f = open('file1.txt', 'a+')
# f.write('ahmed')
# f.close()
# x = open('file1.txt' , 'r')
# for i in x :
#     print(i)




# import  os
# if os.path.exists('file1.txt'):
#     os.remove('file1.txt')
#     print('file 1 deleted')
# else:
#     print('file not found ')

# import os
# if os.path.exists('mydir'):
#     os.rmdir('mydir')
#     print('deleted ')
# else:
#     print('kkkkkk')





# x = lambda :2+10
# print(x())


# f=open(file='file1.txt',mode='r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())




# f=open(file='file1.txt',mode='r')
# for i in f:
#     print(i)


# f=open(file='file1.txt',mode='r')
# print(f.read())



# f = open('file1.txt' , 'w')
# f.write('farhad')
# f.close()
# f = open('file1.txt' , 'r')
# print(f.read())



# f = open(file='file1.txt', mode='a')
# f.write('\nfarhad')
# f.close()
# f = open('file1.txt' , 'r')
# print(f.read())





# import os
# os.remove('file1.txt')


# import os
# if os.path.exists('file1.txt'):
#     os.remove('file1.txt')
#     print('Deleted')
# else:
#     print('file not found ')



# import os
# if os.path.exists('mydir'):
#     os.rmdir('mydir')
# else:
#     print('Folder not found ')

import os
f = open('C:\\Users\\Saman\\Desktop\\shaha.txt' , 'r')
print(f.read())
f.close()
if os.path.exists('C:/Users/Saman/Desktop/shaha.txt'):
    os.remove('C:/Users/Saman/Desktop/shaha.txt')
else:
    print('File not found ')