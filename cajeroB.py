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
             # Módulo 3 (Seleccion de servicio contiene el submodilo 3.1, 3.2, 3.3 y 3.4)
            user_select=input("RETIRO\nTRANSFERENCIA\nCONSULTA\nDEPOSITO\nEscribe una opcion: ")
            #submodulo 3.1 (Retiro de efectivo)
            if user_select == "RETIRO":
                retiro_user=int(input("Ingresa la catindad que desea retirar: "))
                if retiro_user <= fondos:
                    fondos=fondos-retiro_user
                    print(f"Retiro: {retiro_user} MX \n Saldo anterior: {fondos + retiro_user}\n Saldo actual: {fondos}")
                    print("Operación exitosa, ATM servicios le desea un excelente día")
                    break
                else:
                    print("No hay fondos suficientes")
                    break
            elif user_select=="TRANSFERENCIA":
                print("Transferencia")
                break
           
            elif user_select=="CONSULTA":
                print("CONSULTA")
                break
            elif user_select=="DEPOSITO":
                print("DEPOSITO")
                break
            else:
                print("Por favor eliga una opcion correcta")
                break
                
                         
        else:
            intentos_nip += 1
            if intentos_nip < 3:
               print(f"Nip incorrecto intento restantes: {3 - intentos_nip}")
            else:
                print("Excedió el número de intentos. Adiós.")
                break
else:
    print("Lo siento Cuenta incorrecta")
    # retiro = float(input("Ingrese la cantidad que desea retirar: "))
 # if retiro <= fondos:  # Modificado para incluir el caso de retiro igual a los fondos
            #     fondos = fondos - retiro
            #     print(f"Retiro: {retiro} MX \n Saldo anterior: {fondos + retiro}\n Saldo actual: {fondos}")
            #     print("Operación exitosa, ATM servicios le desea un excelente día")
            #     break
            # else:
            #     print("No hay fondos suficientes.")
            #     break