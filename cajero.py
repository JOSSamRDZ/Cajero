print("Bienvenido a ATM Services")
card_verification = 8989

# Módulo 1 (Verificación de cuenta e ingreso de NIP)
card_account = int(input("Ingrese Tarjeta: "))
if card_account == card_verification:
    print("Verificación de cuenta correcta")
    nip_verification = 1425
    intentos_nip = 0
    while intentos_nip < 3:  
        nip_user = int(input("Ingresa NIP: "))
        if nip_user == nip_verification:
            print("NIP correcto")
            fondos = 14000
            retiro = float(input("Ingrese la cantidad que desea retirar: "))
            # Módulo 3 (Verificación de fondos y finalización del programa)
            if retiro <= fondos:  
                fondos = fondos - retiro
                print(f"Retiro: {retiro} MX \n Saldo anterior: {fondos + retiro}\n Saldo actual: {fondos}")
                print("Operación exitosa, ATM servicios le desea un excelente día")
                break
            else:
                print("No hay fondos suficientes.")
                break
        else:
            intentos_nip += 1
            if intentos_nip < 3:
               print(f"Nip incorrecto intento restantes: {3 - intentos_nip}")
            else:
                print("Excedió el número de intentos. La cuenta fue bloqueada.")
                break
else:
    print("Lo siento Cuenta incorrecta")
