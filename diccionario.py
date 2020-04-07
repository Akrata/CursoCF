diccionario = {}
diccionario["nombre"] = "Codigo"#Para agregar una llave con su valor

valor = diccionario["nombre"]#obtener valor 

diccionario["nombre"] = 90 #modificar el valor

diccionario = {"a": 1, "b": 2, "c": 3}

resultado = "z" in diccionario#devuelve False ya que Z no se encuentra en el diccionario

resultado = diccionario.get("a")#retorna el valor
resultado = diccionario.get("z", "La llave no existe")#retorna si la llave no existe la segunda opcion-
resultado = diccionario.setdefault("z","valor")#en caso no exista genera la llave


resultado = diccionario.keys()#devuelve las llaves del diccionario.

resultado  = diccionario.values()#nos devuelve un objeto de tipo dic values. nos devulve valores, hay q convertirlo a lista/tupla

resultado = diccionario.items()#nos devuelve objeto con llaves y valor, habria q convertirlo a tuplas/lista

del diccionario["a"]# elimina la llave A y su valor
valor = diccionario.pop("b")#elimina la llave tambien, y nos retorna el valor eliminado
diccionario = {}# se elimina diccionario.
diccionario.clear()#elimina diccionario
