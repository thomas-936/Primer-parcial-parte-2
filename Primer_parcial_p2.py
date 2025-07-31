print("Primer parte 2")
opcion = 0

def M_C_D(numero1, numero2):
    if numero1 == 0:
        return numero2
    if numero2 == 0:
        return numero1
    else:
        resultado = numero1 % numero2
        resultado2 = numero2 % numero1
        return M_C_D(resultado, resultado2)

def repetitiva(palabra1, veces):
    if veces == 1:
        return palabra1
    else:
        resultado = repetitiva(palabra1, veces - 1)
        return  resultado + repetitiva(palabra1, veces - 1)
def contar_digitos(digito):
    if digito< 10:
        return  1
    else:
        return  1+contar_digitos(digito//10)

def contador(cadena, letra):
    if letra in cadena:
        return  cadena.count(letra)

while opcion != 6:
    print("+++MENU+++")
    print("1. Calcular el MCD")
    print("2. Crear una cadena repetida N veces")
    print("3. Contar cuntas veces aparece una letra en una cadena")
    print("4. Convertir un número decimal a binario")
    print("5. Calcular cuantos digitos tiene un núemero")
    print("6. Salir...")
    try:
        opcion = int(input("Ingrese su Opcion: "))
    except ValueError:
        print("ERROR, Ingrese un dato valido")

    match opcion:
        case 1:
            print("Cualcular el MCD")
            n1 = int(input("Ingrese  el primer núemero: "))
            n2 = int(input("Ingrese el segundp núemero: "))
            print(f"El resultado es: {M_C_D(n1, n2)}")

        case 2:
            print("Crear un cadena repetiva N veces")
            palabra = input("Ingrese una palabra: ")
            veces = int(input("¿Cuantas veces desea que se repita?: "))

            print(f"{repetitiva(palabra, veces)}")
        case 3:
            print("Contar cuantas veces aparece una letra en una cadena ")
            cadena= input("Ingrese un una palabra: ")
            letra = input("Ingrese la letra que desea contar: ")
            print(f"En la cadena {cadena} la letra {letra} se repite: {contador(cadena, letra)} veces")

        case 4:
            print("Convertir un núemero decimal a bianrio ")

        case 5:
            print("Calcular cuantos digitos tiene un nùmero")
            digito = int(input("\nIngrese un nùmero: "))
            print(f"La cantidad de digitos que tiene el número {digito} es: {contar_digitos(digito)}")

        case 6:
            print("Saliendo del programa...")

        case _:
            print("Ingrse un Opción Valida.")