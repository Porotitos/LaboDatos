import numpy as np
import matplotlib as plt

#1
def pertenece (s,e):
    for i in range(0,len(s)):
        if s[i]==e:
            return True
    return False

a1=np.array([1,2,3])
print(pertenece(a1,2))

#2
def mas_larga(s,t):
    if len(s)>len(t):
        return s
    else:
        return t

a2=np.array([1,2,3])
b2=np.array([1,2])
print(mas_larga(a2,b2))

#3
def mezclar(s,t):
    i=0
    j=0
    res=""
    while i<len(s) and j<len(t):
        res=res+s[i]+t[j]
        i+=1
        j+=1
    while i<len(s):
        res=res+s[i]
        i+=1
        while j<len(t):
            res=res+s[j]
            j+=1
    return res

a3="holasss"
b3="chau"
print(mezclar(a3,b3))

#4
"""
def deuda(monto,tasaAnual,plazoMensual,plazo):
    total=monto
    for i in range(0,plazo*12):
        total=(total-plazoMensual)
        total=total+total*tasaAnual/1200
    return total

print(deuda(500000,5,2684.11,30))
"""

#5
#medio trucheli porque no separa en sílabas, ver
def enJeringoso (palabra):
    vocales=np.array(['a','e','i','o','u','A','E','I','O','U'])
    res=""
    for i in range (0,len(palabra)):
        res=res+palabra[i]
        if pertenece(vocales,palabra[i]):
            res=res+"p"+palabra[i]
    return res            

print(enJeringoso("hola mi amigo"))

def traductor_Jeringoso(s): 
    res=[]
    for i in range (0,len(s)):
        print(enJeringoso(s[i]))
        res=res+[s[i]+": "+enJeringoso(s[i])]
    return res

a5=["banana","manzana","mandarina"]
print(traductor_Jeringoso(a5))


#6
def tablasDeMultiplicar (inicio, final):
    print("   ", end=" ")
    for i in range (inicio, final+1):          
        print(f'{i:3}', end=" ")
    for i in range (inicio,final+1):
        print()
        print(f'{i:2}:', end=" ")
        res=i
        if(inicio==0): 
            print(" ",end=" ")
        for j in range(inicio,final+1):
            if j==0:
                print("0", end=" ")
            else: 
                print(f'{res:3}', end=" ")   
                res+=i
            
#ver si se debería poder extender a cualquier rango de números

    
    