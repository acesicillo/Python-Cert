#Variable
test = "David Moreno Cerdas"

#Indexing
print(test[0])

#Slicing
print(test[0:5])

#Next lines are the same thing
print(test[0:len(test)])
print(test[0:])

#We can use steps (steps of 3 in this example)
#Start index, end index and step value.
print(test[0:10:3])

#Print string backwards
print(test[::-1])