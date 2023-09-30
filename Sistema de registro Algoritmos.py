import json
import os
from datetime import datetime, timedelta


tareas_pendientes_archivo = "tareas_pendientes.json"
tareas_completadas_archivo = "tareas_completadas.json"


def cargar_lista_tareas(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as file:
            return json.load(file)
    else:
        return []


def guardar_lista_tareas(tareas, archivo):
    with open(archivo, 'w') as file:
        json.dump(tareas, file, indent=4)


def ejecutar_programa():
    lista_tareas_pendientes = cargar_lista_tareas(tareas_pendientes_archivo)
    lista_tareas_completadas = cargar_lista_tareas(tareas_completadas_archivo)

    while True:
        print("Menu")
        print("1.Agregar una tarea")
        print("2.Lista de tareas pendientes")
        print("3.Marcar tarea como completada")
        print("4.Salir")


        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea(lista_tareas_pendientes)
        elif opcion == "2":
            listar_tareas(lista_tareas_pendientes)
        elif opcion == "3":
            marcar_completada(lista_tareas_pendientes, lista_tareas_completadas)
        elif opcion == "4":
            guardar_lista_tareas(lista_tareas_pendientes, tareas_pendientes_archivo)
            guardar_lista_tareas(lista_tareas_completadas, tareas_completadas_archivo)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def agregar_tarea(lista_tareas):
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (opcional - formato: YYYY-MM-DD): ")

    tarea = {"titulo": titulo, "descripcion": descripcion, "completada": False}

    if fecha_vencimiento:
        tarea["fecha_vencimiento"] = fecha_vencimiento

    lista_tareas.append(tarea)
    print("Tarea agregada con éxito!")


def listar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas disponibles.")
    else:
        for i, tarea in enumerate(lista_tareas, 1):
            print(f"{i}. Título: {tarea['titulo']}")
            print(f"   Descripción: {tarea['descripcion']}")
            if "fecha_vencimiento" in tarea:
                print(f"   Fecha de vencimiento: {tarea['fecha_vencimiento']}")
            print()


def marcar_completada(lista_tareas_pendientes, lista_tareas_completadas):
    listar_tareas(lista_tareas_pendientes)
    try:
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice < len(lista_tareas_pendientes):
            tarea_completada = lista_tareas_pendientes.pop(indice)
            tarea_completada["completada"] = True
            lista_tareas_completadas.append(tarea_completada)
            print("Tarea marcada como completada!")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

if __name__ == "__main__":
    ejecutar_programa()
