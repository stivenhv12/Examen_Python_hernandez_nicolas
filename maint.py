
from calculos import calcular_propina_simple,calcular_propina_dividida
def menu_principal():
    while True:
        print("""=============================================
  SIMULADOR DE PROPINA
=============================================
1. Calcular propina y total a pagar
2. Calcular total a pagar divido entre varias personas
3. Salir
=============================================""")
        
        opcion = input("Por favor, elige una opción (1-3): ")

        if opcion == '1':
            calcular_propina_simple()
        elif opcion == '2':
            calcular_propina_dividida()
        elif opcion == '3':
            print("=============================================")
            print("¡gracias por usar el simulador de propina!")
            print("=============================================")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")



menu_principal()