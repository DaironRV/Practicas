# # condicional if

# dato = int(input("ingresa un nimero: "))

# if dato>0 :
#     print("numero positivo")
#     print("segundo resultado positivo")
# elif dato == 0 :
#     print("el numero es 0")
# else: 
#     print("el numero es negativo")


# numero = int(input("nimgresa el numero: "))
# numero2 = int(input("ingresa el nuemro: "))


# if numero%2==0 and numero2%2==0: 
#     print(f"el {numero} y el {numero2} son par")
# elif numero%2==0: 
#     print(f"solo el {numero} es par")
# elif numero2%2==0: 
#     print(f"solo el {numero2} es par")
# else:
#     print("ninguno de los dos es par")


# if numero % numero2 == 0: 
#     print("es multiplo")
# else: 
#     print("no es multiplo")


# el .is_integer, compara el numeor de la variable "resultado", si el numero que da la variable tiene algo que no sea un ,0 despue de la "," da false
# if resultado.is_integer(): 
#     print("estos numeros son multiplos")
# else: 
#     print("estos numeros no son multiplos")


n1 = int(input("ingresa el primer nuemro: "))
n2 = int(input("ingresa el segundo nuemor: "))
n3 = int(input("ingresa el tercer nuemor: "))

if n1>n2 and n1>n3: 
    print(f"el {n1} es el mayor")
elif n2>n1 and n2>n3: 
    print(f"el es {n2} el mayor")
else:
    print(f"el {n3} es el mayor")
