#dictionary
ages = {"David":34,"Pamela":31,"Roxana":35,"David2":33}
print(ages)

#access values
print(ages["David"])

#Add value to dict
ages["Jose"] = 31
print(ages)

#reassign values
ages["Jose"] = 30
print(ages)

#remove values
del ages["Jose"]
print(ages)

#verify key:value exists
print("David" in ages)
print("Jose" in ages)

#ways to create dictionaries
weights = dict(david=100,pame=200,jose=300)
print(weights)

#with a list of tuples
colors = dict([("david","blue"),("pame","purple"),("jose","black")])
print(colors)

#METHODS
#get the keys
print(colors.keys())

#make a list with the keys of a dict
print(list((colors.keys())))

#get the values
print(colors.values())

#make a list with the values of a dict
print(list((colors.values())))

#make a list of the items of a dict
print(list(colors.items()))