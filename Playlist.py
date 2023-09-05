import random

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        self.estado = "detenido"
        self.indice_actual = -1

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f'Canción "{cancion}" agregada a la playlist.')

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            print(f'Canción "{cancion}" eliminada de la playlist.')
        else:
            print(f'Canción "{cancion}" no encontrada en la playlist.')

    def mostrar_canciones(self):
        print("Lista de canciones:")
        for i, cancion in enumerate(self.canciones, 1):
            print(f'{i}. {cancion}')

    def reproducir(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "reproduciendo"
            print(f'Reproduciendo: {self.canciones[self.indice_actual]}')
        else:
            print("Índice de canción no válido.")

    def seleccionar_cancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            print(f'Se seleccionó la canción: {self.canciones[self.indice_actual]}')
        else:
            print("Índice de canción no válido.")

    def pausar(self):
        if self.estado == "reproduciendo":
            self.estado = "pausa"
            print("Reproducción en pausa.")
        else:
            print("La reproducción no se puede pausar en este momento.")

    def detener(self):
        if self.estado == "reproduciendo" or self.estado == "pausa":
            self.estado = "detenido"
            self.indice_actual = -1
            print("Reproducción detenida.")
        else:
            print("La reproducción no se puede detener en este momento.")

    def siguiente(self):
        if self.estado == "reproduciendo":
            if self.indice_actual < len(self.canciones) - 1:
                self.indice_actual += 1
                print(f'Siguiente canción: {self.canciones[self.indice_actual]}')
            else:
                print("No hay más canciones en la lista.")
        else:
            print("La reproducción no se puede avanzar en este momento.")

    def anterior(self):
        if self.estado == "reproduciendo":
            if self.indice_actual > 0:
                self.indice_actual -= 1
                print(f'Canción anterior: {self.canciones[self.indice_actual]}')
            else:
                print("No hay canciones anteriores en la lista.")
        else:
            print("La reproducción no se puede retroceder en este momento.")

    def reproducir_aleatorio(self):
        if self.estado != "reproduciendo":
            cancion_aleatoria = random.choice(self.canciones)
            self.indice_actual = self.canciones.index(cancion_aleatoria)
            self.estado = "reproduciendo"
            print(f'Reproduciendo aleatoriamente: {cancion_aleatoria}')
        else:
            print("Ya se está reproduciendo una canción.")

    def ver_estado(self):
        print(f'Estado: {self.estado}')

    def ver_cancion_actual(self):
        if self.estado == "reproduciendo":
            print(f'Canción actual: {self.canciones[self.indice_actual]}')
        else:
            print("No se está reproduciendo ninguna canción.")


mi_playlist = Playlist("Mi Playlist")


while True:
    print("Menú:")
    print("1-Agregar canción")
    print("2-Eliminar canción")
    print("3-Mostrar canciones")
    print("4-Reproducir canción")
    print("5-Seleccionar canción")
    print("6-Pausar reproducción")
    print("7-Detener reproducción")
    print("8-Siguiente canción")
    print("9-Canción anterior")
    print("10-Reproducir canción aleatoria")
    print("11-Ver estado de la playlist")
    print("12-Ver canción actual")
    print("13-Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cancion = input("Ingrese el nombre de la canción a agregar: ")
        mi_playlist.agregar_cancion(cancion)
    elif opcion == "2":
        cancion = input("Ingrese el nombre de la canción a eliminar: ")
        mi_playlist.eliminar_cancion(cancion)
    elif opcion == "3":
        mi_playlist.mostrar_canciones()
    elif opcion == "4":
        indice = int(input("Ingrese el índice de la canción a reproducir: "))
        mi_playlist.reproducir(indice - 1)
    elif opcion == "5":
        indice = int(input("Ingrese el índice de la canción a seleccionar: "))
        mi_playlist.seleccionar_cancion(indice - 1)
    elif opcion == "6":
        mi_playlist.pausar()
    elif opcion == "7":
        mi_playlist.detener()
    elif opcion == "8":
        mi_playlist.siguiente()
    elif opcion == "9":
        mi_playlist.anterior()
    elif opcion == "10":
        mi_playlist.reproducir_aleatorio()
    elif opcion == "11":
        mi_playlist.ver_estado()
    elif opcion == "12":
        mi_playlist.ver_cancion_actual()
    elif opcion == "13":
        break
    else:
        print("Opción no válida. Intente de nuevo.")


