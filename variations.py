#Python implementation here

message = input("Enter a message: ")
print("Uppercase:",message.upper())
print("Lowercase:",message.lower())
print("Capitalized:",message.capitalize())
print("Title Case:",message.title())

words = message.split()
print(words)

sorted_words = sorted(words)
print("Alphabetic 1st Word",sorted_words[0])
print("Alphabetic last Word",sorted_words[-1])

if "David" in message:  
    print("Hola David")
else:
    print("Quien eres?")

print(ord("A"))
print(ord("Z"))
