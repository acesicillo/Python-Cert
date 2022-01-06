name = input("Digite Nombre: ")
color = input("Digite Color Favorito: ")
edad = int(input("Digite Edad: "))

#By default Print send a new line
print(name)
print("Le gusta el color " + color + " y tiene")
print(str(edad) + " años")

#We can change print end with end=" "
print(name,end=" ")
print("Le gusta el color " + color + " y tiene",end=" ")
print(str(edad) + " años")

#We can change print end with sep=" "
print(name, "le gusta el color "+ color, "y tiene", str(edad) + "años", sep=", ")