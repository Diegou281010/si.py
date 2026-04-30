import random
import string

print("Bienvenido al sistema de creación de contraseñas.")

letras_minusculas = list(string.ascii_lowercase)
letras_mayusculas = list(string.ascii_uppercase)
numeros = list(string.digits)

longitud_contraseña = int(input("Ingrese la longitud deseada para la contraseña: "))
caracteres = letras_minusculas + letras_mayusculas + numeros
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud_contraseña))


print("Nueva contraseña creada exitosamente.")

print("Tu nueva contraseña es:", contraseña)