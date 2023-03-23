# Hallar la suma de los primeros N numeros narurales 


# input 
N = int(input("Digite el valor de N: "))
suma = 0
i = 1

# processing
while (i<=N):
    suma = suma+i
    i = i+1

print("suma es: " + str(suma))
    