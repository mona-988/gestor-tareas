def agregar_tarea(lista, tarea):
 lista.append(tarea)
 return lista

def listar_tareas(lista):
 for i, t in enumerate(lista, 1):
  print(f"{i}. {t}")
     
 def eliminar_tarea(lista, indice):
   if 0 <= indice < len(lista):
    lista.pop(indice)
   return list
