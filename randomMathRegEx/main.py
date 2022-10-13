# import random
# random.seed(10)
# print(random.randint(a=1,b=9))
# random.seed(22)
# print(random.randint(3,7))
# random.seed(113)
# print(random.randint(2,5))


# import random as r
# x = r.randint(22,44)
# print(x)


# import random as r
# x = r.randrange(22,44)
# print(x)

#
# import random as r
# x = r.random()
# print(x)


# import random as r
# mylist = ['saman' ,'attalla ' , 'haji','emad' ]
# x = r.choice(mylist)
# print(x)


# import random as r
# mylist = ['saman' ,'attalla ' , 'haji','emad' ]
# x = r.choices(mylist,k=2)
# print(x)



# import random as r
# mylist = ['saman' ,'attalla ' , 'haji','emad' ]
# r.shuffle(mylist)
# print(mylist[1])



# import random as r
# mylist = ['saman' ,'attalla ' , 'haji','emad' ]
# x = r.sample(mylist, k=3)
# print(x)
# for i in range(len(x)):
#     print(x[i])



# import math as m
#
# print(round(9.4))






# import re
# txt = "aThe rain in Spain"
# x = re.findall(r"in\b", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")




# import re
# txt = "aThe rain in Spain"
# x = re.findall(r"ai\B", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# import re
# txt = "The 3 rain in 5 Spain 9"
# x = re.findall("\d", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")



# import re
#
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
#
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")






# import re
# txt = "The rain in Spain"
# x = re.findall("\S", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")




# import re
# txt = "The rain in Spain"
# x = re.findall("[a-r]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")




# import re
# txt = "The rain in Spain"
# x = re.findall("[^ari]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")



# import re
# txt = "The 4 rain 2in 1Spain"
# x = re.findall("[012]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")






#
# import re
#
# txt = " sam yes "
# x = re.search("\s", txt)
#
# print("first match", x.start())




# import re
#
# txt = "The rain in Spain"
# x = re.split("\s", txt,3)
# print(x)




# import re
#
# txt = "The rain in Spain"
# x = re.sub("[n]", "$", txt)
# print(x)





# import re
#
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.span())


# import re
#
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.string)


#
#
#
# import re
#
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.group())





# import random
# random.seed(18)
# print(random.randint(100, 200))
# random.seed(222)
# print(random.random())
# random.seed(345)
# print(random.random())


#
# import random
# random.seed()
# print(random.randint(1,5))





# import random
# x = random.randrange(11,15)
# y = random.randint(a=2,b=9)
# print(x)
# print(y)


# import random
# mylist= ['saman' ,'talib', 'lava' ,'marwan']
# print(random.choice(mylist))


# import random
# mylist= ['saman' ,'talib', 'lava' ,'marwan']
# print(random.choices(mylist,k=3))

# import random
# mylist= ['saman' ,'talib', 'lava' ,'marwan']
# random.shuffle(mylist)
# print(mylist)


#
# import random
# mylist= ['saman' ,'talib', 'lava' ,'marwan']
# print(random.sample(mylist,k=2))



# import random
# print(random.uniform(5,9))






# import math
# print(math.floor(5.9))
# print(math.ceil(5.1))
# print(round(5.4))
# print(math.pow(4,3))
# print(math.sqrt(4))
# print(math.factorial(5))
# print(math.factorial(4))




# import re
#
# txt = "The rain in Spain lava"
# x = re.findall("[a-d]", txt)
# print(x)

# import re
#
# txt = "hello planet helava"
# x = re.findall("he...a", txt)
# print(x)
#
# import re
#
# txt = "helpo planet"
# x = re.findall("he.*", txt)
# print(x)

#
# import re
#
# txt = "helllo planet"
# x = re.findall("hel{3}o", txt)
# print(x)




# import re
# txt = "The rain in Spain"
# x = re.findall("\AThe", txt)
# print(x)
#
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")




# import re
# txt = "The Therain in TheSpain"
# x = re.findall(r"\bThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")









# import re
# txt = "The raThein in TheSpain"
# x = re.findall(r"The\B", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")




# import re
# txt = "The ra8in i4n Sp3ain"
# x = re.split(r"\d", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")




# import re
# txt = "The raThein in TheSpain"
# x = re.sub(r"\s",'$', txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")






# import re
# txt = "The rain in Spain"
# x = re.findall(r"[^aT]", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")









# import re
# txt = "The rain* in +Spain"
# x = re.findall(r"[*+]", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")\


# import re
#
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)




# import re
#
# txt = "The rain in Spain"
# x = re.sub("[i]", "#", txt , 2)
# print(x)



# import re
#
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.span())



# import re
#
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.string)




import re

txt = "The rain in Spain"
x = re.search("i", txt)
print(x.group())










