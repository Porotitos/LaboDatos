
empleado_01=[[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000]]
empleado_02=[[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000],[43967304,37,0,12000],[42236276,36,0,18000]]
empleado_03=[[20222333,20000,45,2],[33456234,25000,40,0],[45432345,10000,41,1],[43967304,12000,37,0],[42236276,18000,36,0]]
empleado_04=[[20222333,33456234,45432345,43967304,42236276],[20000,25000,10000,12000,18000],[45,40,41,37,36],[2,0,1,0,0]]
#ƖuƭƈrƞƑSaƩƄrƦoAƆƱƌvƦƇaơ01
def superanSalarioActividad01(matriz,umbral):
    res=[]
    for fila in matriz:
        if fila[3]>=umbral:
            res=res+[fila]
    return res

print(superanSalarioActividad01(empleado_02,15000))

def superanSalarioActividad03(matriz,umbral):
    res=[]
    for fila in matriz:
        if fila[1]>=umbral:
            res=res+[[fila[0],fila[2],fila[3],fila[1]]]
    return res

print(superanSalarioActividad03(empleado_03,15000))

def superanSalarioActividad04(matriz,umbral):
    res=[]
    for i in range(0,len(matriz[1])):
        if matriz[1][i]>=umbral:
            res=res+[[matriz[0][i],matriz[2][i],matriz[3][i],matriz[1][i]]]
    return res

def traspuesta(matriz):
    res=[]
    for i in range(0,len(matriz[0])):
        res+=[[]]
        for fila in matriz:
            res[i]+=[fila[i]]
    return res

print(traspuesta(empleado_01))

print(superanSalarioActividad04(empleado_04,15000))

#1.a. no generó ningún problema porque el programa funciona independientemente de la cant de filas
#1.b. una vez alterado el orden de columnas tuvo un problema porque el programa está hecho para leer especificamente la columna
#que tiene los salarios

#2.idem com 1b
#3.