
grades = [4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 2]
#Como filtar los números pares y los impares?

#pares
even = []

#impares
odd = []

#Es par cuando el resto o residuo de dividir al numero es 2 es 0
for grade in grades: 

    if grade% 2 == 0:
        even.append(grade)
    else:
        odd.append(grade)

print(f"Los pares son {even}")
print(f"Los impares son: {odd}")
