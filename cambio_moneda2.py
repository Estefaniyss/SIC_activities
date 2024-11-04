''' ¿Qué sucede si la cantidad de monedas para el cambio es limitada?
    Ejem: Se tiene almacenado para el cambio la siguiente cantidad;
    1 de 500w, 1 de 100w, 3 de 50w y 2 de 10w.
    - ¿ Cómo se debe distribuir 710 para el cambio ?
'''

def cambio_moneda2(monedas, cant):
    cambios = []
    mayor = 0
    while cant > 0 and mayor < len(monedas):
        if cant < monedas[mayor][1]:
            mayor += 1
        else:
            if monedas[mayor][0] > 0:
                cambios.append(monedas[mayor][1])
                cant -= monedas[mayor][1]
                monedas[mayor][0] -= 1
            else:
                mayor += 1
    return cambios

monedas = []
for i in range(4):
    sublista = list(map(int, input("Ingrese las monedas almacenadas: ").split())) 
    monedas.append(sublista)

print(monedas)
cant = int(input("Introduzca monto: "))
cambios = cambio_moneda2(monedas, cant)
suma = 0
for i in cambios:
    suma += i
if cant > suma:
    print(-1)
else:
    print(cambios, len(cambios))