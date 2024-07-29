def algoritmo (numero_tarjeta):
    digits = [int(caracter) for caracter in str(numero_tarjeta)]

    for i in range (len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    suma_total = suma_total = sum(digits)    

    return suma_total % 10 == 0


# Listas tarjetas
tarjetas = [3379513561108795, 
            6011000990139424, 
            5555555555554444, 
            371449635398431]

#Validar cada tarjetiña de la lista
for tarjeta in tarjetas:
    if algoritmo(tarjeta):
        print(f"La tarjeta {tarjeta} es válida.")
    else:
        print(f"La tarjeta {tarjeta} no es válida.")
