
"""
Maquina expendedora V1
"""
import os
import csv


MONEDA = 'Euro_1'
BOLA = 'Bola entregada'
CAPACIDAD = 100 #Numero de bolas que caben en el deposito
RUTA = '/home/raulsg/Desktop/proyecto_maquina_expendedora/maquinabolas/ '

class MaquinaBolas():
    """Clase que representa la maquina"""

    def __init__(self) -> None:
        self.deposito = CAPACIDAD
        self.monedero = 0

    def aceptar_moneda(self,moneda_insertada):
        """Metodo para aceptar una moneda y devuelve true o false dependiendo si es correcta"""
        return moneda_insertada == MONEDA

    def girar_manivela(self,giro):
        """Simula el giro de la manivela de la maquina.
           Solo funciona con giros de 360º"""
        return giro == 360

    def soltar_bola(self):
        """Si se ha insertado una moneda valida y la manivela gira correctamente,
           se suelta una bola de chicle.
           Se decrementa el numero de bolas.
           Se incrementa el numero de monedas"""
        self.deposito -= 1
        self.monedero += 1
        return BOLA

    def salvar_estado(self):
        """Guarda el estado actual tanto del deposito
        como del monedero en un fichero csv para
        recuperarlo al volver a iniciar la maquina"""
        with open(RUTA + 'estado_maquina.csv') as csv_writer:
            escritor = csv.writer(csv_writer)
            escritor.writerow([self.deposito])
            escritor.writerow([self.monedero])

    def leer_estado(self):
        with open(RUTA + 'estado_maquina.csv') as manejador:

         
