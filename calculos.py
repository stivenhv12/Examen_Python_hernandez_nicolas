def calcular_propina(total, porcentaje):
    return total * (porcentaje / 100)

def calcular_propina_simple():
    while True:
        print("\n=============================================")
        print("  calculo de propina")
        print("=============================================")
        try:
            total = float(input("Ingrese el monto total de la cuenta: $"))
            porcentaje = float(input("Ingrese el porcentaje de propina(%): "))
            
            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)

            print("=============================================")
            print(f"La propina calculada es: ${propina:.2f}")
            print(f"El total a pagar es: ${total_con_propina:.2f}")
            print("=============================================")

            repetir = input("¿Deseas calcular nuevamente? (S/N): ").lower()
            if repetir != 's':
                break

        except ValueError:
            print("Error: Ingresa valores numéricos válidos.")

def calcular_total_con_propina(total, propina):
    return total + propina

def dividir_total(total, personas):
    if personas == 0:
        return 0
    return total / personas

def calcular_propina_dividida():
    while True:
        print("\n=============================================")
        print("  Dividir Cuenta entre Varias Personas")
        print("=============================================")
        try:
            total = float(input("Ingrese el monto total de la cuenta: $"))
            porcentaje = float(input("Ingrese el porcentaje de propina(%): "))
            personas = int(input("Ingrese el número de personas: "))

            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)
            monto_por_persona = dividir_total(total_con_propina, personas)

            print("=============================================")
            print(f"La propina calculada es: ${propina:.2f}")
            print(f"El total a pagar es: ${total_con_propina:.2f}")
            print(f"Monto por persona: ${monto_por_persona:.2f}")
            print("=============================================")

            repetir = input("¿Deseas calcular nuevamente? (S/N): ").lower()
            if repetir != 's':
                break

        except ValueError:
            print("Error: Ingresa valores numéricos válidos.")