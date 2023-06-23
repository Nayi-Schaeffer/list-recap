grades = [4, 5, 6, 7, 8, 3, 4, 5, 6, 7, 2]
sum = 0
for grade in grades:
    sum += grade

print(f"El promedio de las notas es:\n {sum/len(grades)}")
