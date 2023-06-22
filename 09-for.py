fruits = ["apple","orange","strawberry","watermelon","pears","mango"]

#for es una variable auxiliar que es para citar de una en una un nombre de una lista.
for fruit in fruits:
    print(f"I like {fruit}")

print("----------------------")


position = 0
while position < len(fruits):
    print(f"I like {fruits[position]}")
    position += 1

