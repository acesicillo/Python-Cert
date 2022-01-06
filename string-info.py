#Lab #2 Indexing and Slicing Phython Strings

message = input("Enter a message: ")
print("First character: ", message[0])
print("Last character: ", message[-1])
print("Middle character: ", message[int(len(message)/2)-1])
print("Even index characters: ", message[0::2])
print("Odd index characters: ", message[1::2])
print("Reverse message: ", message[::-1])


