#listas
l=[22,True,"una lista",[1,2]]
print(l)
print(l[0])
m=["una lista",[1,2]]
print(m)
print(m[1][0]) 
b=[22,True]
b[0]=99
print(b[0])
#tuplas los elementos no se pueden desordenar
t= 1,2,3
type(t)
tupla=(4,"Hola,",4)
print(tupla)
#diccionario
diccionario={}
print(diccionario)
#se utiliza para darle un significado a una palabra
diccionario={"azul":"blue", "rojo":"red"}
print(diccionario)
print(diccionario["azul"]) #para mostrar el valor de una clave
diccionario["amarillo":"yellow"] # para añadir un nuevo elemento
diccionario["azul"]="BLUE" # modificar un elementp
del(diccionario["rojo"]) #para elminar una clave
agenda={"Alejandro":[22,1.78],"David":[34,1,54]}

