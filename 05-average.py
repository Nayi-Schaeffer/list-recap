
grades = []
menu_option = ""
while menu_option !="3":
    print("Calculadora de promedios")
    print("1. Agregar nota")
    print("2. Calcular promedio")
    print("3. Salir")

    menu_option = input()

    if menu_option == "1":
        number = float(input("Ingresa la nota: \n"))
        grades.append(number)
    elif menu_option == "2":
        #suamr todas las notas y dividir por la cantidad
        #Acumulador
        sum = 0
        for grade in grades:
            sum += grade
            print(f"El promedio de las notas es:\n {sum/len(grades)}")
        
        

    elif menu_option =="3":
        print("Adios")
    else:
        print("Ingrese algo valido")

      

    
    

