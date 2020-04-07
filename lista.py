cursos = ["python", "django", "flask", "c", "c#"]

curso = cursos[0]
curso = curso[-1] # = c#
print(curso)


sub = cursos[0:3]# contiene 3 elementos. tambien se puede escribir como [:3], tambien se puede alrevez, [5:]

sub = cursos [1:7:2]# genera saltos de 2 en 2 entre la lista.

sub = cursos [::-1]#Se genera la lista alrevez


lista = [8.17, 90, 1,5,44,1.32]
lista.sort()#ordena la lista
lista.sort(reverse=True)#ordena alrevez
menor = min(lista)#numero menor
mayor = max(lista)#numero mayor
longitud = len(lista)#longitud.

resultado = 8.17 in lista #Devuelve valor booleano.

indice = lista.index(8.17)#nos regresa el indice donde esta

conteo = lista.count(5)#nos devuelve la cantidad de veces que se encuentra en la lista, si no esta devuelve 0.

####------------mATRIZ---------------####

fila_uno = [10, 20]
fila_dos = [30, 40]

matriz = [fila_uno, fila_dos]

primer_elemento = matriz[0][0]