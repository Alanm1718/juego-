import random
def generar_numero_secreto():
    
    digitos = list(range(10))   
    random.shuffle(digitos)
    

    numero = ''.join(map(str, digitos[:4]))
    

    if numero[0] == '0':
        for i in range(1, 4):
            if numero[i] != '0':
                lista_numero = list(numero)
                lista_numero[0], lista_numero[i] = lista_numero[i], lista_numero[0]
                numero = "".join(lista_numero)
                break
                
    return numero

def validar_numero(numero):
    
    numero = numero.strip()
    
    if not numero.isdigit():
        return False, "Epaaa! Solo debes ingresar números."
    if len(numero) != 4:
        return False, "Debe tener exactamente 4 dígitos."
    if len(set(numero)) != 4:
        return False, "Los dígitos no pueden repetirse."
    
    return True, ""


def obtener_pistas(numero_jugador, numero_secreto):
    
    
    vacas = sum(1 for i in range(4) if numero_jugador[i] == numero_secreto[i])
    
    toros = sum(1 for i in range(4) if numero_jugador[i] in numero_secreto and numero_jugador[i] != numero_secreto[i])
    pistas = []
    pistas.append(" Vaca " * vacas)
    pistas.append(" Toro " * toros)
    
    pista_final = ''.join(pistas).strip()
    
    if not pista_final:
        return "No hay mas  pistas. Sigue intentando jejej"
    return pista_final


def jugar():


    MAX_INTENTOS = 10 
    
    numero_secreto_elegido = generar_numero_secreto()
    intentos = 0 
    
    print("      ¡BIENVENIDO!")
    print("-"*50)
    print("Tengo un número en mente de 4 dígitos sin repetir.")
    print(f"¡Tienes un máximo de {MAX_INTENTOS} intentos para adivinarlo!")
    print("-"*50)
    print("REGLAS:") 
    print("Vaca = un dígito correcto en la posición correcta")
    print("Toro = un dígito correcto en la posición incorrecta")

    while True:
        intentos += 1
        if intentos > MAX_INTENTOS:
        
            print("¡OH NO! se ha terminado los intentos si quiere seguir compra el plus .")
            print(f"El número secreto era: {numero_secreto_elegido}")
        
            break 
            
        entrada = input(f"Intento {intentos}/{MAX_INTENTOS}: Ingrese el número de 4 dígitos: ")
        
        valido, mensaje = validar_numero(entrada)
        
        if not valido:
            print(f" Algo no esta bien : {mensaje}")
            intentos -= 1 
            continue
            
        if entrada == numero_secreto_elegido:
            print("\n" + "-"*50)
            print(f"¡¡¡NDE VALE !!!")
            print(f"Lo has logrado en {intentos} intentos.")
            print("-"*50 + "\n")
            break
            
        pistas = obtener_pistas(entrada, numero_secreto_elegido)
        print(f"Pistas: {pistas}")
        

if __name__ == "__main__":
    jugar()