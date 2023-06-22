

shopping_list = []
menu_option = ""

while menu_option != "4":
    print("La lista de compras\n")
    print("1. Agregar")
    print("2  Quitar")
    print("3. Ver")
    print("4. Salir")

    menu_option =(input())

    if menu_option == "1":
       #Agregamos elementos a la lista
       shopping_list.append(input("Ingresa el elemto que quieras agregar:\n"))

    elif menu_option == "2":
        element = input("Ingresa el elmento que quieras eliminar:\n")
        shopping_list.remove(element)

    elif menu_option == "3":
     #Mostrar todo el contenido de shopping_list
     print("Tu listado de compras tiene lo siguiente:\n")
     for item in shopping_list:
         print(item) 

    elif menu_option == "4":
        print("Chao Chao\n")

    else:
        print("Selecciona una opción válida")

        

