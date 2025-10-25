notas = []
historial =[]
revision =[]

def registrar_curso_y_nota():
    curso = input ("Ingresar el nombre del curso:").strip()

    if curso == "":
        print ("El nombre del curso no puede estar vacio.")
        return
    
    entrada = input ("Ingrese la nota del surso (0-100:)")
## validar que la entrada sea un numero
    if not entrada.isnumeric():
        print("La nota deber estar entre el numero 0 y 100.")
        return
    nota = int(entrada)
    if 0 <= nota <= 100:
     notas.append ({"curso": curso, "nota": nota})
     historial.append(f"registro curso'{curso}'con nota{nota}")
     print("curso y nota registrados correctamente.")
    else:
       print("La nota debe estar entre 0 y 100.")

## Funcion que muestre todas las notas registradas
def mostrar_notas():
   if len(notas) == 0:
      print("No hay notas registradas.")    
   else:
      print("Notas registradas:")
      for contador, registro in enumerate(notas,start=1):
         print(f"{contador}. curso:{registro["curso"]}, nota:{registro["nota"]}")

## funcion para calcular y mostrar el promedio de las notas 
def calcular_promedio ():
   if len (notas) == 0:
      print("No existen datos para calular el promedio")
   else:
      suma = 0
      for registro in notas:
         suma += registro["nota"]
         promedio = suma / len(notas)
      print(f"el promedio de las notas son: {promedio:.2f}")

## Funcion para buscar uno de los cursos
def buscar_curso():
    if len(notas) == 0:
        print("No hay notas registradas para buscar.")
        return
    
    curso_buscar = input("Ingrese el nombre del curso que desea buscar: ").strip()

    for registro in notas:
        if registro["curso"].lower() == curso_buscar.lower():
            print(f"Curso encontrado: {registro['curso']}, Nota: {registro['nota']}")
            historial.append(f"buscar curso'{registro['curso']}' con nota {registro['nota']}")
            return
    print("Curso no encontrado.")

## funcion para actualizar las notas existentes 
def actualizar_notas():
   if len(notas) == 0:
          print("No existen notas registradas para actualizar.")
          return

   mostrar_notas()
   posicion = input("Ingrese el número del curso que desea actualizar: ")
    
   if not posicion.isnumeric():
        print("Entrada inválida. Por favor, ingrese un número válido.")
        return
    
   posicion = int(posicion)
   if 1 <= posicion <= len(notas):
        nueva_nota = input("Ingrese la nueva nota (0-100): ")
        if not nueva_nota.isnumeric():
            print("La nota debe ser un número entre 0 y 100.")
            return
        
        nueva_nota = int(nueva_nota)
        if 0 <= nueva_nota <= 100:
            notas[posicion - 1]['nota'] = nueva_nota
            historial.append(f"Actualizó nota del curso '{notas[posicion - 1]['curso']}' a {nueva_nota}")
            print("Nota actualizada exitosamente.")
        else:
            print("La nota debe estar entre 0 y 100.")

# elimminacion de cursos 
def eliminar_curso():
    if len(notas) == 0:
        print("no hay cursos registrados")
        return
    
    mostrar_notas()
    posicion = input("Ingrese numero del curso que desea eliminar: ")

    if not posicion.isnumeric():
        print("Debe ingresar un numero valido")
        return
    posicion = int(posicion)
    if 1 <= posicion <= len(notas):
        eliminado = notas.pop(posicion - 1)
        historial.append(f"elimino curso'{eliminado['curso']}' con nota {eliminado['nota']}")
        print(f"Curso {eliminado['curso']} eliminado exitosamente.")
    else:
        print("Posición inválida.")

## pila y cola 
def ver_historial():
    if len(historial) == 0:
        print ("historial vacio")
    else:
        print("historial de acciones(ultima primero)")
        for accion in reversed(historial):
            print(f"-{accion}")

def agregar_revision():
    curso = input("ingresar el curso a revision:").strip()
    if curso == "":
        print("el curso no debe estar bacio error:")
        return
    revision.append(curso)
    historial.append(f"agrego curso'{curso}' a la lista de revicion")
    print(f"el curso{curso} agregar a la lista de revision.")

def procesar_revision():
    if len(revision) == 0:
        print ("no hay en la lista de revicion.")
    else:
        curso = revision.pop(0)
        historial.append(f"procesar revicion del curso '{curso}'")
        print(f"iniciando revicion del curso:{curso}")

## ordenamiento 
def ordenar_burbuja():
    if len(notas) == 0:
        print("no existen notas registradas para ordenar.")
        return
    
    lista = notas.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]['nota'] > lista[j+1]['nota']:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    print("curso ordenado por nota(burbuja):")
    for registro in lista:
        print(f"- {registro['curso']}: {registro['nota']}")

def ordenar_insercion():
    if len(notas) == 0:
        print("no existen notas registradas para ordenar.")
        return
    
    lista = notas.copy()
    for i in range(1, len(lista)):
        key = lista [i]
        j = i-1
        while j >= 0 and key['nota'] < lista [j]['nota']:
            lista [j + 1] = lista [j]
            j -= 1
        lista[j + 1] = key  
    
    print("cursos ordenados por nota (insercion):")
    for registro in lista:
        print(f"-{registro['curso']}:{registro['nota']}")

def buscar_estudiante_existente():
    estudiante = input("Ingrese el nombre del estudiante:").strip()
    if estudiante == "":
        print("El nombre del estudiante no puede estar vacio.")
        return 
    estudiantes_existentes = ["Ana", "Luis", "Maria", "carlos"]

    if estudiante.capitalize() in estudiantes_existentes:
       print(f"El estudiante {estudiante.capitalize()} existe en el sistema.")
    else:
        print(f"El estudiante{estudiante.capitalize()} no existe en el sistema.")

def buscar_seccion_estudiante():
    estudiante = input("Ingrese el nombre del estudiante:").strip()
    if estudiante == "":
        print("el nombre del estudiante no puede estar vacio.")
        return
    if estudiante.capitalize() in secciones:
        print(f"El estudiante {estudiante.capitalize()} pertenece a la sección {secciones[estudiante.capitalize()]}.")
    else:
        print(f"El estudiante {estudiante.capitalize()} no existe en el sistema.")
secciones = {
    "Ana": "A",
    "Luis": "B",
    "Maria": "A",
    "Carlos": "C"
}
    

def menu():
 while True:
    print("\nMenú de opciones:")
    print("1. Registrar curso y nota")
    print("2. Mostrar notas registradas")
    print("3. Calcular promedio de notas")
    print("4. buscar curso")
    print("5. Actualizar nota de un curso")
    print("6. Eliminar curso")
    print("7. ver historial")
    print("8. agregar curso a revicion")
    print("9. procesar revicion de curso")
    print("10. ordenar notas (burbuja)")
    print("11. ordenar notas (insercion)")
    print("12. Buscar estudiantes existentes")
    print("13. Buscar sección estudiante")
    print("14. Salir")
    
    opcion = input("Seleccione una opción (1-14): ")
    
    if opcion == "1":
        registrar_curso_y_nota()
    elif opcion == "2":
        mostrar_notas()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        buscar_curso()
    elif opcion == "5":
        actualizar_notas()
    elif opcion == "6":
        eliminar_curso()
    elif opcion == "7":
        ver_historial()
    elif opcion == "8":
        agregar_revision()
    elif opcion == "9":
        procesar_revision()
    elif opcion == "10":
        ordenar_burbuja ()
    elif opcion == "11":
        ordenar_insercion()
    elif opcion == "12":
        buscar_estudiante_existente()
    elif opcion == "13":
        buscar_seccion_estudiante()
    elif opcion == "14":
        print("Feliz dia, Gracias por usar el gestor de notas academicas")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 14.")
menu()