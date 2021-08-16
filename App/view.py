"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 """

from os import curdir
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")

    # TODO: Modificaciones para el laboratorio 1.
    print("3- Cargar Libros Etiquetados")

    print("0- Salir")


def loadBooks():
    """
    Carga los libros
    """
    return controller.loadBooks('GoodReads/books-small.csv')


def loadTags():
    """
    Carga los Tags
    """
    return controller.loadTags('GoodReads/tags.csv')

# Definición función que carga los libros etiquetados.
def loadBooksTags():
    """
        Carga los libros etiquetados. 
        
        Queda pendiente:
        1- Editar la función loadBookTags del módulo controller.py para que sirva su propósito.

    """
    return controller.loadBooksTags('GoodReads/book_tags.csv')


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de libros....")
        books = loadBooks()
        print('Total de libros cargados: ' + str(lt.size(books)))

    elif int(inputs[0]) == 2:
        print("Cargando información de tags....")
        tags = loadTags()
        print('Total de tags cargados: ' + str(lt.size(tags)))


    # TODO: Modificaciones para el laboratorio 1.
    elif int(inputs[0]) == 3:
        """
            Este elif no hará nada, solo imprimirá el mensaje de carga. Se comentó
            la línea 106 para que no se produzca ningún error (en este caso, se podría
            producir un error porque la función loadBooksTags retorna None, y la función 
            size solo admite como argumento a valores de tipo list).

        """
        print("Cargando información de libros etiquetados....")
        booksTags = loadBooksTags()
        # print('Total de libros etiquetados cargados: ' + str(lt.size(booksTags)))


    else:
        sys.exit(0)
sys.exit(0)