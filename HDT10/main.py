from functions import read_graph_from_file, print_shortest_path, calculate_center_of_graph, modify_graph

filename = "logistica.txt"
graph, cities = read_graph_from_file(filename)

while True:
    print("\nOpciones:")
    print("1. Encontrar la ruta más corta entre 2 ciudades")
    print("2. Calcular el centro del grafo")
    print("3. Modificar el grafo")
    print("4. Salir")
    option = int(input("Ingrese una opción: "))

    if option == 1:
        print("\nCiudades disponibles (Colocar nombre como se observa):")
        for city in cities:
            print(city)
        city1 = input("Ingrese la ciudad de origen: ").strip()
        city2 = input("Ingrese la ciudad de destino: ").strip()


        if city1 not in cities or city2 not in cities:
            print("Una o ambas ciudades ingresadas no existen en la lista de ciudades.")
        else:
            print_shortest_path(graph, city1, city2, cities)

    elif option == 2:
        center_index = calculate_center_of_graph(graph)
        print("Centro del grafo:", cities[center_index])

    elif option == 3:
        modify_graph(graph, cities, filename)

    elif option == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")