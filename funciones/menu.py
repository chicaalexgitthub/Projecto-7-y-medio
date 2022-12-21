from data import *

"""Menu = menu que queremos imprimir por pantalla.
   lista = opciones validas."""


def menus(menu, lista):
    # Imprimimos el menu deseado por pantalla.
    print(menu)
    # Pedimos al usuario que introduzca la opcion deseada.
    opt = input("\nOption: ")
    try:
        # Comprobamos que la opcion introducida sea digito.
        if not opt.isdigit():
            # Si la opcion no es digito generamos un error.
            raise TypeError("The option must be a digit.")
        # Comprobamos que la opcion se encuentre la lista de opciones validas.
        elif not int(opt) in lista:
            # Si no se encuentra en la lista generamos un error.
            raise ValueError("Invalid option.")
        # Si llegamos hasta aqui al opcion es valida asi que la devolvemos.
        return int(opt)
    # En caso de error.
    except TypeError as error:
        # Imprimimos el mensaje de error.
        print(error)
        # Paramos el programa hasta que se pulse enter.
        input("Press enter to continue.")
        # Llamamos de vuelta a la funcion.
        menus(menu, lista)
    except ValueError as error:
        # Imprimimos el mensaje de error.
        print(error)
        # Paramos el programa hasta que se pulse enter.
        input("Press enter to continue.")
        # Llamamos de vuelta a la funcion.
        menus(menu, lista)



