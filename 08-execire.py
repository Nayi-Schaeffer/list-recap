#Cada estudiante del arreglo student tiene sus calificaciones en el arreglo grades, manteniendo su posicion.


students = ["Ignacia", "Poulette", "Vane", "Jazz", "Tuguitugui"]
curse_grades = [[5,6,4,5,6],[5,6,7,4,5],[5,6,4,5,6],[4,5,6,5,4],[5,6,4,5,6]]

#Se pide un programa que imprima el nombre de la estudiante, junto con el promedio de sus notas.

for student, grades in zip (students, curse_grades):
    sum = 0
    for grade in grades:
        sum += grade

    print(f"El promedio de la estudiante {student} es: {sum/len(grades)}")

