# row = 6  # صف
# column = 10  # عامود
# for i in range(0, row):
#     for j in range(0, column):
#         print(end=' ')
#     column = column - 2
#     for j in range(0, i+2):
#         print("* ", end='')
#     print()

row = 5
column = 0
for i in range(1 , row+1):
    for j in range(1, (row-i)+1):
        print(end=' ')
    while  column != (2*i - 1):
        print("*", end='')
        column = column +1
    column = 0
    print()
column = 2
m = 1
for i in range(1,row):
    for j in range(1, column):
        print(end=' ')
    column += 1
    while m <= (2 * (row - i)- 1):
        print('*' , end='')
        m=m+1
    m=1
    print()

# 21 KOTELK
# 0 1 1 2 3 5 8 13 21