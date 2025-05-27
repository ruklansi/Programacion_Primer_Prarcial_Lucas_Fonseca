# main.py
import os
from Funciones import *
from Inputs import validar_nombre

# Inicialización
array_nombres = crear_array(5, "")
matriz_puntajes = crear_matriz(5, 3, 0)
bandera_carga_nombres = False
bandera_carga_puntajes = False

while True:
    print("1. Cargar Participantes")
    print("2. Cargar Puntuaciones")
    print("3. Mostrar Puntuaciones")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Top 3 participantes")
    print("12. Participantes ordenados alfabéticamente")
    print("13. Salir")
    
    try:
        opcion = int(input("Su opción (1-13): "))
        if opcion < 1 or opcion > 13:
            print("Error: Opción inválida.")
            input("Toque cualquier tecla para continuar...")
            os.system("clear")
            continue
    except ValueError:
        print("Error: Ingrese un número entero.")
        input("Toque cualquier tecla para continuar...")
        os.system("clear")
        continue

    if opcion == 1:
        if cargar_nombres_participantes(array_nombres):
            print("Nombres cargados correctamente...")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error al realizar la carga")
    
    elif opcion == 2:
        if cargar_puntajes(matriz_puntajes):
            print("Carga exitosa de puntajes!")
            mostrar_matriz(matriz_puntajes)
            bandera_carga_puntajes = True
        else:
            print("Error al realizar la carga")
    
    elif opcion == 3 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_puntajes(array_nombres, matriz_puntajes):
            print("Error al mostrar las puntuaciones")
    
    elif opcion == 4 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_participantes_menor_promedio(matriz_puntajes, array_nombres, 4):
            print("No hay participantes con promedio menor a 4")
    
    elif opcion == 5 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_participantes_menor_promedio(matriz_puntajes, array_nombres, 8):
            print("No hay participantes con promedio menor a 8")
    
    elif opcion == 6 and bandera_carga_nombres and bandera_carga_puntajes:
        promedios = promedio_por_jurado(matriz_puntajes)
        for i, prom in enumerate(promedios):
            print(f"Promedio Jurado {i + 1}: {prom}")
    
    elif opcion == 7 and bandera_carga_nombres and bandera_carga_puntajes:
        jurados = jurado_mas_estricto(matriz_puntajes)
        if jurados:
            print("Jurado(s) más estricto(s):", ", ".join(f"Jurado {j}" for j in jurados))
        else:
            print("No se pudieron calcular los jurados más estrictos")
    
    elif opcion == 8 and bandera_carga_nombres and bandera_carga_puntajes:
        jurados = jurado_mas_generoso(matriz_puntajes)
        if jurados:
            print("Jurado(s) más generoso(s):", ", ".join(f"Jurado {j}" for j in jurados))
        else:
            print("No se pudieron calcular los jurados más generosos")
    
    elif opcion == 9 and bandera_carga_nombres and bandera_carga_puntajes:
        if not participantes_puntajes_iguales(matriz_puntajes, array_nombres):
            print("No hay participantes con puntuaciones iguales")
    
    elif opcion == 10 and bandera_carga_nombres and bandera_carga_puntajes:
        nombre = validar_nombre()
        if not buscar_participante_por_nombre(array_nombres, matriz_puntajes, nombre):
            print(f"No se encontró al participante {nombre}")
    
    elif opcion == 11 and bandera_carga_nombres and bandera_carga_puntajes:
        if not top_3_participantes(array_nombres, matriz_puntajes):
            print("Error al mostrar el top 3")
    
    elif opcion == 12 and bandera_carga_nombres and bandera_carga_puntajes:
        if not participantes_ordenados_alfabeticamente(array_nombres, matriz_puntajes):
            print("Error al mostrar los participantes ordenados")
    
    elif opcion == 13:
        print("Saliendo...")
        break
    
    else:
        print("Acceso inválido: Debe cargar nombres y puntajes primero")
    
    input("Toque cualquier tecla para continuar...")
    os.system("clear")