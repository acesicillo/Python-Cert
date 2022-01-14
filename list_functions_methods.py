my_list = [11,7,1]
print(my_list)

#By default the appended item goes to the end
my_list.append(4)
print(my_list)

#to add an item in an especific position else, we need insert method, 1st argument is index, 2nd is value to be added
my_list.insert(2,43)
print(my_list)

#Return the index value if the value exist on the list
print(my_list.index(7))

#Check value in the list, return boolean
print(5 not in my_list)
print(4 not in my_list)
print(3 in my_list)

#Functions reversed and sorted, must be same type of elements, cant mix int and str
print(list(reversed(my_list)))
print(sorted(my_list))

#Matrix
my_matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
row_count = (len(my_matrix))
column_count = (len(my_matrix[0]))
print(my_matrix)
print(row_count)
print(column_count)
print(my_matrix[0][1])

#Same rows and columns is a cube
print(row_count == column_count)
