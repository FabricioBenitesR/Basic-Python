def selector_actividades (s, f):
    n = len(s)
    A = [0]
    j = 0
    print(j)
    for i in range (1, n):
        if (s[i] >= f[j]):
            print(i)
            A.append(i)
            j = i
    return A

n1 = int(input('Ingrese la cantidad de actividades: '))

s1 = []
f1 = []

for a in range (0, n1):
    valS1 = int(input(f'Ingrese el valor de la matriz S: '))
    s1.append(valS1)

for b in range (0, n1):
    valF1 = int(input(f'Ingrese el valor de la matriz F: '))
    f1.append(valF1)

actividadesCompatibles = selector_actividades (s1, f1)
print('Las actividades seleccionadas son: ', actividadesCompatibles)
