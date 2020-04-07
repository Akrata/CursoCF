curso = "Curso de python 3"

resultado = len(curso)#cuantos caracteres tiene este string


resultado = curso[0]#buscar por indice

#los strings son inmutables, no se pueden cambiar.

#GENERAR UNA LISTA A PARTIR DE UN STRING
lenguajes = "python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

resultado = lenguajes.split()#separa por espacio los lenguaje en strings,
resultado = lenguajes.split(";")#separa por ; los lenguaje en strings,
#o podemos hacer

separador = "; "
resultado = lenguajes.split(separador)



#Generar un string a partir de una lista.

nuevo_string = " ".join(resultado)#me genera un string con el separador indicado.


texto = """esto es un texto
con saltos
de linea"""

resultado = texto.splitlines()#te genera una lista con los strings en cada salto de linea.


#####

texto = "curso de python 3"

resultado = texto.capitalize()#genra un nuevo string con la primera letra en MAYS
resultado = texto.swapcase()#Cambia las minusculas a mayusculas y las mayusculas a minusculas.
resultado = texto.upper()#todas las letras a mays
resultado = texto.lower()#todo a minus
texto.isupper()
texto.islower()#retorna boolean


resultado = texto.replace("python","ruby")#cambia el primer valor por el segundo, si ponemos un 3er valor es la cantidad de veces que quiero que remplaze la palabra
resultado = texto.strip()#quita los espacios al principio y a final.


###########################

curso = "Python"
version = "3"

resultado = "Curso de %s %s" %(curso, version)#llenar con variables


resultado = "Curso de {} {}".format(curso,version)#las llaves se remplazan por los valores
resultado = "Curso de {b} {a}".format(a=curso,b=version)#tambien se le puede asignar variable a vada una de las llaves.