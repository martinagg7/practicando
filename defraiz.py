
import math
#si pido los parametros en el bloque principal luego los paso  a la funcion
def raiz(a,b,c):
    dentro_raiz=b**2-4*a*c
    if dentro_raiz>0:
        solucion_1=(b+math.sqrt(dentro_raiz))//2
        solucion_2=(b-math.sqrt(dentro_raiz))//2
        numerosoluciones=2
    elif dentro_raiz==0:
        solucion_1=b//2
        solucion_2=solucion_1
        numerosoluciones=1
    else:
        solucion_1=0
        solucion_2=0
        numerosoluciones=0
    return solucion_1,solucion_2,numerosoluciones

