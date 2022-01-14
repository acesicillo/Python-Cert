my_string = "Testing"
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())

my_title = "This is a multiword string"
print(my_title.title())

#Verify string is ASCII, titled, digit, space
print(my_string.isascii())
print(my_string.istitle())
print(my_string.isdigit())
print(my_string.isspace())

#Verify a string can be used as variable
print(my_string.isidentifier())
print(my_title.isidentifier())

#Separate string words
phrase = "This is a simple phrase"
print(phrase.split())

url = "https://example.com/users/david"
print(url.split("/")[-1])
print((url.split("/")))

#join strings into a single one
lines = ["1st","2nd","3rd"]
print("-".join(lines))
print(".".join(lines))
print("\n".join(lines))

#Replace {} with values given in the format() method.
template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
print(template.format("David","Python"))

#can be done also with index
template = "Hello, my name is {0}, and I really enjoy {1}, Have a nice day!, {0}."
print(template.format("David","Python"))

