# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "gender" : "Female" ,
#            "result":True}
#
# print(student['first_name'] +" "+ student['last_name'] +" "+ str(student['result'] ))


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "gender" : "Female" ,
#            "result":True}
#
# print(student.keys())


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "gender" : "Female" ,
#            "result":True}
#
# print(student.values())



# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "gender" : "Female" ,
#            "result":True}
#
# print(dir(student))



# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True}
# student['age'] = 20
# student['result']= False
# print(student['age'])
# print(student['result'])
# student.update({"result":True})
# print(student['result'])

# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True}
# student['stage']= 4
# print(student['stage'])




# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True }
# student.update({'stage' : "Graduated"})
# print(student['stage'])


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True }
# student.update({'stage' : "Graduated"})
# print(student['stage'])


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated"}
# student.pop('result')
# print(student.values())





# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated"}
# del student['result']
# print(student.values())


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated"}
# student.clear()
# print(student.values())


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated" }
# p = student.copy()
# print(p.values())



# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated" }
# final_result = student.get('first_name')
# print("Congratulation Mrs " + final_result)


# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated" }
# final_result = student['result']
# print("Congratulation Mrs " + str(final_result))

# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            "result":True ,'stage' : "Graduated" }
# final_result = student.items()
# print( final_result)
# print( student)


#
# student = {"id" : 1  , "first_name" : "Basma",
#            "last_name": "alyas" , "age":18,"gender" : "Female" ,
#            'stage' : "Graduated" }
# student.setdefault('result', False)
# print(student)



