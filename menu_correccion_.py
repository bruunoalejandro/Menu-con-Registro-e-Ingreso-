usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None
opcion = 0
user = 0
contador = 0
while opcion != 3:
    print("\tMenu de Ingreso")
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
    except:
        print("La opción debe ser numerica")
    if opcion == 1:
        if user == 0:
            print("Usted debe registrarse.")
        else:
            nombre = input("Ingrese nombre de usuario: ")
            if usuario1 == nombre:
                password = int(input("Ingrese contraseña: "))
                
                if password == contrasena1:
                        while opcion != 3:
                            print("\tBienvenido(a), que deseas hacer? ")
                            print("1) Realizar llamada")
                            print("2) Enviar correo electrónico")
                            print("3) Cerrar sesión")
                            try:
                                x = int(input("Elija una opción: "))
                            except:
                                print("La opción debe ser numerica")
                            if x < 1 and x > 3:
                                print("Numero de opcion incorrecta. ")
                            if x == 1:
                                print("Ingrese numero de telefono: ")
                                tel = int(input())
                                while tel < 900000000 or tel > 999999999:
                                    print("Ingresaste un numero no valido")
                                    tel = int(input("Ingrese numero de telefono: "))
                                print("Llamando a...", tel)
                                input("Presione Enter para continuar")
                            if x == 2:
                                correo = input("Ingrese correo electronico: ")
                                contador = 0
                                for i in correo:
                                    if i == "@":
                                        contador = contador + 1
                                mensaje = input("Ingrese mensaje: ")
                                print("Enviando mensaje:\n" + mensaje + "\nAl correo: " + correo)
                            while contador != 1:
                                print("El correo solo debe tener un @")
                                correo = input("Ingrese correo electronico: ")
                                contador = 0
                                for i in correo:
                                    if i == "@":
                                        contador = contador + 1
                                mensaje = input("Ingrese mensaje: ")
                                print("Enviando mensaje:\n" + mensaje + "\nAl correo: " + correo)
                            if x == 3:
                                print("Encerrando tu sesion...")
                                break
                else:
                    print("Ingrese la contraseña correcta")
            if usuario2 == nombre:
                password = int(input("Ingrese contraseña: "))
                if password == contrasena2:
                    print("Bienvenido.")
                else:
                    print("Contraseña incorrecta.")
            if usuario3 == nombre:
                password = int(input("Ingrese contraseña: "))
                if password == contrasena3:
                    print("Bienvenido")
                else:
                    print("Contraseña incorrecta.")
    if opcion == 2:
        if user < 3:
            if user == 0:
                usuario1 = input("Ingrese nombre de usuario: ")
                try:
                    contrasena1 = int(input("Ingrese contraseña: "))
                    user = user + 1
                except:
                    print("Debe ingresar solo numeros")
            elif user == 1:
                usuario2 = input("Ingrese nombre de usuario: ")
                try:
                    contrasena2 = int(input("Ingrese contraseña: "))
                    user = user + 1
                except:
                    print("Debe ingresar solo numeros")
            elif user == 2:
                usuario3 = input("Ingrese nombre de usuario: ")
                try:
                    contrasena3 = int(input("Ingrese contraseña: "))
                    user = user + 1
                except:
                    print("Debe ingresar solo numeros")
        else:
            print("Se llego al maximo de numero de usuarios registrados permitidos...")
print("Hasta luego :) ")