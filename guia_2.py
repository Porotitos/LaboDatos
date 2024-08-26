import pandas as pd
import numpy as np
import csv

#1
def leer_parque(nombre_archivo, parque):
    lista_arboles = []
    with open(nombre_archivo, 'rt', encoding="utf8") as archivo:
        filas = csv.reader(archivo)
        encabezado=next(filas)
        for fila in filas:
            if fila[10] == parque:
                registro=dict(zip(encabezado,fila))
                lista_arboles.append(registro)
                
    return lista_arboles

#print((leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ')))


#2
def especies(lista_arboles):
    conjunto=set()
    for elem in lista_arboles:
        conjunto.add(elem['nombre_com'])
    return conjunto

#a=leer_parque('arbolado-en-espacios-verdes.csv','GENERAL PAZ')
#b=leer_parque('arbolado-en-espacios-verdes.csv','CENTENARIO')
#c=leer_parque('arbolado-en-espacios-verdes.csv','ANDES, LOS')
#print(especies(a))

#3
def contar_ejemplares(lista_arboles):
    res={}
    for elem in lista_arboles:
        if elem["nombre_com"] not in res:
            res[elem["nombre_com"]]=1
        else:
            res[elem["nombre_com"]]+=1
    return res

#print(contar_ejemplares(b))

#4
def obtener_alturas(lista_arboles, especie):
    res=[]
    for elem in lista_arboles:
        if elem["nombre_com"]==especie:
            res.append(float(elem["altura_tot"]))
    return res

def promedio (lista):
    sumatoria=0
    for elem in lista:
        sumatoria+=elem
    return sumatoria/len(lista)

def maximo (lista):
    maxim=lista[0]
    for elem in lista:
        if elem>maxim:
            maxim=elem
    return maxim

#print(promedio(obtener_alturas(a,"Jacarandá")))
#print(maximo(obtener_alturas(a,"Jacarandá")))

#5
def obtener_inclinaciones(lista_arboles,especie):
    res=[]
    for elem in lista_arboles:
        if elem["nombre_com"]==especie:
            res.append(float(elem["inclinacio"]))
    return res

#6
def especimen_mas_inclinado(lista_arboles):
    mayorIncli=0.0
    mas_inclinado=""
    for especimen in especies(lista_arboles):
        comparado=maximo(obtener_inclinaciones(lista_arboles,especimen))
        if comparado>mayorIncli:
            mayorIncli=comparado
            mas_inclinado=especimen
    return mayorIncli,mas_inclinado

#print(especimen_mas_inclinado(b))

#7
def especie_promedio_mas_inclinada(lista_arboles):
    mayorIncli=0.0
    mas_inclinado=""
    for especimen in especies(lista_arboles):
        comparado=promedio(obtener_inclinaciones(lista_arboles,especimen))
        if comparado>mayorIncli:
            mayorIncli=comparado
            mas_inclinado=especimen
    return mayorIncli,mas_inclinado

#print(especie_promedio_mas_inclinada(c))
df1=pd.read_csv("arbolado-en-espacios-verdes.csv",
                usecols=['nombre_cie', 'diametro',
                         'altura_tot'],
                header=0)
df2=pd.read_csv("arbolado-publico-lineal-2017-2018.csv", 
               usecols=['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho',
                        'altura_arbol'],
               header=0)

especies_seleccionadasdf1 = ['Tilia viridis subsp. x moltkei', 'Jacarandá mimosifolia', 'Tipuana Tipu']
especies_seleccionadasdf2 = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

#8 ver de optimizar las condiciones sobre filas
df_tipas_parques=df1.loc[(df1["nombre_cie"]=='Tilia viridis subsp. x moltkei') | (df1["nombre_cie"]=='Jacarandá mimosifolia') | (df1["nombre_cie"]=='Tipuana Tipu'), ["altura_tot","diametro"]].copy()
df_tipas_parques.rename(columns={"altura_tot":"Altura","diametro":"Diametro"}, inplace=True)
df_tipas_parques["ambiente"]="parque"

df_tipas_veredas=df2.loc[(df2["nombre_cientifico"]=='Tilia x moltkei') | (df2["nombre_cientifico"]=='Jacaranda mimosifolia') | (df2["nombre_cientifico"]=='Tipuana tipu'), ["altura_arbol","diametro_altura_pecho"]].copy()
df_tipas_veredas.rename(columns={"altura_arbol":"Altura","diametro_altura_pecho":"Diametro"}, inplace=True)
df_tipas_veredas["ambiente"]="vereda"

    
Final=pd.concat([df_tipas_parques,df_tipas_veredas])

print(df_tipas_parques["Altura"].mean())
print(df_tipas_veredas["Altura"].mean())

print(df_tipas_parques["Diametro"].mean())
print(df_tipas_veredas["Diametro"].mean())
