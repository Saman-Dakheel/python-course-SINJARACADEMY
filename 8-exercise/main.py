#1- Store a message in a variable, and print that message.
# Then change the value of your variable to a new message, and print the new
# message.
#solve
# message = "This is my message"
# print(message)
# message = "message changed"
# print(message)


#2- Store a person’s name in a variable, and then print that
# person’s name in lowercase, uppercase, and titlecase.
# name = input("Enter Your Name: ")
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.count("saman"))


# Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output
# should look something like the
# following, including the quotation marks:
# Albert Einstein once said, "A person who never made a
# mistake never tried anything new."

#
# qoute = "Albert Einstein once said, \nA person who never made a mistake never tried anything new.\""
# print(qoute)
# q = "it is\tfor \nnew line \'single qoute"
# print(q)


#  Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

# name = input("Enter your name: ")
# new_name = f"your name is {name}\n you are welcome with us"
# print(new_name)
# x = name.strip() # lstrip() , rstrip()
# print(x)



# If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner

# list1 = ['zakria' , "talib" , 'dler']
# print(f"welcome to dinner {list1[0]}")
# print(f"welcome to dinner {list1[1]}")
# print(f"welcome to dinner {list1[2]}")
# list1.clear()
# list1.append("lava")
# list1.append("marwan")
# list1.append("mazin")
# print(f"welcome to dinner {list1[0]}")
# print(f"welcome to dinner {list1[1]}")
# print(f"welcome to dinner {list1[2]}")
# list1.insert(0,"sabah")
# print(f"welcome to dinner {list1[0]}")




# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your
# dictionary. Think of a favorite number for each person,
# and store each as a value in your dictionary. Print each
# person’s name and their favorite number. For even more
# fun, poll
# a few friends and get some actual data for your program.

fav_num = {
    "saman":3,
    "sabah":2,
    "najya":6
}

print(f"your favorite number is {fav_num['saman']}")
print(f"your favorite number is {fav_num['sabah']}")
print(f"your favorite number is {fav_num['najya']}")