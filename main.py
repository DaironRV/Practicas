

# print ("Hola mundo de nuevo") 
# print ("Hola habla Dairon")

# # tipos de datos: 

# # Init
# numero = 52
# print (numero)
# print(type(numero))

# # string
# palabra = "Hola mundo"
# print (palabra)
# print(type(palabra))

# # booleano
# dato = True 
# print(dato)
# print(type(dato))

# # float
# numero2 = 2.3
# print(numero2)
# print(type(numero2))


# # el input es para ingresar cualquier cosa en la consola, ya sea un numero o un string
# # nombre = input("cual es tu nombre ")
# # print ("hola " + nombre)


# # asi funcionan el if y el else
# # nombre2 = input("cual es tu nombre ")
# # if nombre2 == "Sara":
# #     print("Hola Sara")
# # else: 
# #     print("no eres Sara chinga tu madre")

# # numero3 = int("123456")
# # print(numero3)

# # numero4 = int(7.9)
# # print(numero4)

# # # el int solo recibe que tengan meramente caracteres numeros, nada de letras o cuaquier otra cosa
# # # nombre4 = int("hola que hace 2")
# # # print (nombre4)

# # numero5 = int(7,9)
# # print(numero4)



# # nombre1 = input("como te llamas? ")
# # print (nombre1) 

# # calculo = input("Cualculame está: ")
# # calculo = int(calculo) #el int tiene que tener siempre una variable
# # if calculo >= 112:
# #     print("el resultado este")
# # else:
# #     print("no le sabes")

# # operadores aritmeticos: 

# # suma: 
# n1 = 5
# n2 = 3 
# c = n1 + n2
# print(c)

# # negación y resta:
# # la negacion son numeros negativos
# n1 = -8

# n1 = 88
# n2 = 99
# c = n1 - n2
# print(c)

# # multiplicación
# n1 = 3
# n2 = 9 
# c = n1 * n2
# print(c)

# # potencia
# n1 = 2 
# n2 = 3 
# c = n1 ** n2
# print(c)

# # divición: 
# n1 = 7 
# n2 = 2
# c = n1 / n2
# print(c)

# # divición entera: Esta divicion solamente te va a mostrar el resultado entero, sin el decimal
# n1 = 7 
# n2 = 2
# c = n1 // n2
# print(c)

# # modulo: es lo que te entra el residio de una divición. O lo que sobra en una divición

# n1 = 9 
# n2 = 3
# c = n1 % n2
# print(c)

# a = 5 
# b = 9 
# c = 3 

# resultado = ((5+9/3)**2)-64
# print(resultado)


# # operadores relacionales

# # operador de compración
# r = 52 == 100
# print(r)

# r = 100 == 100
# print(r)

# # distinto que:
# # esto siempre va a dar un true o false. Si el resultado da True, graciasa a "!=" ahora sera un false

# r = (100 != 100)
# print(r)

# # menor que / menor o igual que: 

# r = (50 < 100)
# print(r)


# r = (100 <= 100)
# print(r)

# # mayor que / mayor o igual que: 

# r = (50 > 100)
# print(r)


# r = (100 >= 100)
# print(r)



# opredores logicos

# # and
# a = 30 
# b = 40
# c= 50

# r = ((a<b)and(b<c))
# print(r)

# # or
# r = ((a<b)or(b>c))
# print(r)

# # not
# r = not (a>b)
# print(r)

# operadores de asignación

# c = 0

# c += 10

# c -=5

# c *= 3

# c //=5

# c /= 5

# c **= 3

# c %= 3

# print(c)

# salida des datos:

# app = "flutter"
# proyecto = "ComFlu"

# print(f"se hara en {app} se llamara {proyecto}")

# c = float(input("caunto equivale c: "))
# b = float(input("caunto equivale b: "))
# a = float(input("caunto equivale a: "))

# resultado = ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

# print(f"tu resultado es {resultado}")

# '''
# por lo mismo del lenguaje es el porque canbia, es masomenos asi
#                                                                     a b
#                                                                     | |
#                                                                     b a
# '''
# a = int(input("a: "))
# b = int(input("b: "))

# a,b=b,a

# print(f"el nuevo a valor es: {a}")
# print(f"el nuevo b valor es: {b}")


# import math

# r = float(input("el valor del radio: "))

# area = math.pi*r**2
# logintud = 2*math.pi*r

# # el :.1if, es la cantidad de datos de que se van a mostrar, en este caso solo era 1 dato 
# print(f"la longitud del circulo es {logintud:.1f}")
# print(f"el area del circulo es {area:.1f}")




# numero = float(input("cual es el precio del producto: "))
# porcentaje = float(input("cual es el porcentaje de descuento que deseas aplicar: "))

# resultado = porcentaje*numero/100
# resultado2 = numero-resultado

# print(f"el precio original del producto es: {numero}")
# print(f"tu porcentaje de descuento es: {porcentaje}%")
# print(f"el resultado de tu descuento es: {resultado2:.2f}")


# los [] son para comparar sus indices, eso va de 0 a lo que tu quieras, simplemente es la cantidad de caracteres de algo se mide en indices

# nombre1= input("agregar nombre 1: ")
# nombre2= input("agregar nombre 2: ")

# if nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]:
#     print("tanto la ultima como la primera letra coinciden")
# elif nombre1[0] == nombre2[0]:
#     print("la primer letar coincide")
# elif  nombre1[-1] == nombre2[-1]: 
#     print("la ultima letra coincide")
# else: 
#     print("ni la primer ni la ultima de las letras coincide")
    



# nombre1 = input("Agregar nombre 1: ")
# nombre2 = input("Agregar nombre 2: ")

# if nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]:
#     print("Tanto la última como la primera letra coinciden")
# elif nombre1[0] == nombre2[0]:
#     print("La primera letra coincide")
# elif nombre1[-1] == nombre2[-1]:
#     print("La última letra coincide")
# else:
#     print("Ni la primera ni la última de las letras coincide")




dinero = 2000
MostrarDinero = dinero

print("Los comandos a tu disposición son:\nAgregar dinero\nReembolso de dinero\nMostrar dinero")

while True:
    acción = input("¿Qué acción deseas hacer?: ")

    if acción == "agregar dinero":
        dineroAgregado = int(input("¿Cuánto dinero deseas agregar? "))
        resultado = dineroAgregado + dinero
        print(f"{resultado} es tu saldo actual.")
        accion = input("¿Qué deseas hacer?: ")
        if accion == "reembolso de dinero":
            cantidad = int(input("de cuanto es el reembolso: "))
            reembolso = resultado - cantidad
            print(f"Saldo: {reembolso}")
        elif accion == "salir":
            print("¡Gracias por usar nuestro servicio!")
            break
    elif acción == "mostrar dinero":
        print(MostrarDinero)
        break
    else:
        print("Opción no válida. Intenta nuevamente.")

print("¡Gracias por usar nuestro servicio!")


# dinero = 2000
# MostrarDinero = dinero

# def mostrar_saldo():
#     print(f"Tu saldo actual es: {MostrarDinero}")

# def agregar_dinero():
#     global dinero
#     dineroAgregado = int(input("¿Cuánto dinero deseas agregar? "))
#     dinero += dineroAgregado
#     mostrar_saldo()

# def reembolso_dinero():
#     global dinero
#     if "dineroAgregado" in locals():
#         reembolso = dineroAgregado
#         dinero -= reembolso
#         print(f"Se ha reembolsado {reembolso}. Tu saldo actual es: {dinero}")
#     else:
#         print("Primero agrega dinero antes de solicitar un reembolso.")

# def main():
#     print("Los comandos a tu disposición son:\nAgregar dinero\nReembolso de dinero\nMostrar dinero")

#     while True:
#         acción = input("¿Qué acción deseas hacer? (o escribe 'salir' para salir): ")

#         if acción == "agregar dinero":
#             agregar_dinero()
#         elif acción == "reembolso de dinero":
#             reembolso_dinero()
#         elif acción == "mostrar dinero":
#             mostrar_saldo()
#         elif acción == "salir":
#             print("¡Gracias por usar nuestro servicio!")
#             break
#         else:
#             print("Opción no válida. Intenta nuevamente.")

# if __name__ == "__main__":
#     main()

