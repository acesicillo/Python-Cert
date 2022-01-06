my_list = [1,2,3,4,5]
print(my_list)

#Lists are muttable
my_list[0] = "a"
my_list[1] = "b"
my_list[2] = "c"
print(my_list)

#indexing
print(my_list[0])
#slicing
print(my_list[:3])
#stepping
print(my_list[::2])

#concatenate
my_list2 = [6,7,8]
my_new_list=my_list+my_list2
print(my_new_list)

#Add more items
my_list+=my_list2
print(my_list)

#mutation with slicing, change first 2 items on the ist
my_list[0:3] = [1,2,3]
print(my_list)
