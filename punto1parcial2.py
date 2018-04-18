# print "El grado del polinomio es: ", n
n=5
matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n
vector[0]=35
vector[1]=48
vector[2]=70
vector[3]=40
vector[4]=22
matriz[0][0]=35
matriz[1][0]=45
matriz[2][0]=55
matriz[3][0]=65
matriz[4][0]=75
punto_a_evaluar = int(input("Ingrese el punto a evaluar: "))

print ("------------------------------")
print ("------- Calculando ... -------")
print ("------------------------------")

for i in range(1,n):
    for j in range(i,n):
        matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))
aprx = 0
mul = 1.0
for i in range(n):
    mul = matriz[i][i];
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
    aprx = aprx + mul

print ("El valor aproximado de f(",punto_a_evaluar,") es: ", -aprx)