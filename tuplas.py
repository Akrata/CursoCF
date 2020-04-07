#no podemos modificar los elementos de una tupla.

tupla = (1,2,3,4,5,6,7,8,9,0)

elemento = tupla[4]#busca en el indice numero 

sub = tupla[:5:2]#genera una tupla con esos parametros

tupla[1] = 20 ##LAS TUPLAS NO SE PUEDEN MODIFICAR SON INMUTABLES

#COMPRIMIR Y DESCOMPRIMIR TUPLAS

tupla = (1,2,3,4)
uno, dos, tres, cuatro = tupla# a cada variable se le asigna el valor del indice en la tupla
tupla = (1,2,3,4,5,6)
uno,dos,tres,*cuatro = tupla[]# genera en la variable con *, una nueva lista con los que no pueden ser asignados a las variables.

uno,*dos,cinco,seis = tupla[]#de esta manera python coloca el indice 1, pasa por alto el valor con * y comienza de atras a adelante, rellenando el * con valores que sobran.

tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla_dos = (100, 200, 300, 400)

resultado = zip(tupla, lista, tupla_dos) #genera un Objeto. con tuplas de 3 elementos 1, 10, 100
resultado = list(resultado)



tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

primero, segundo, *_, ultimo = tupla# con el _ podemos NO guardar nada en esa variable.