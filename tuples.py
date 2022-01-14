#tuples
#tuples are immutable

my_tuple = (1,2,3)
x,y,z = my_tuple
print(x,y,z)

print("My name is:  %s %s" % ("David","Moreno"))

person1=("David Moreno","34","83222808")
person2=("Pamela Mora","31","85109957")

print(person1[0])

#combining lists and tuples
my_list=[1,2,3]
my_tuple2 = (my_list,1)
print(my_tuple2)
other_list=(1,2,my_tuple2,3,4)
print(other_list)

#we cant modify the tuple, but we can modify mutable items inside the tuple
#like a list 

my_list.append(4)
print(my_tuple2)
