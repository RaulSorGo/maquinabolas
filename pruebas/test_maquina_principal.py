"""
Pruebas de la clase Maquina
"""
import unittest
from maquina_principal import MaquinaBolas, MONEDA, BOLA

class TestMaquina(unittest.TestCase):
    """pruebas"""
    def test_creacion_maquina(self):
        """prueba de existencia de la clase"""
        maquina = MaquinaBolas()
        self.assertIsNotNone(maquina)

    def test_moneda_1e_es_valida(self):
        """ Prueba de moneda de un Euro es correcta"""
        maquina = MaquinaBolas()
        resp = maquina.aceptar_moneda(MONEDA)
        self.assertEqual(resp, True)

    def test_moneda_50cent_es_invalida(self):
        """ Prueba de moneda de 50 cents es incorrecta"""
        maquina = MaquinaBolas()
        resp = maquina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False)

    def test_giro_manivela_correcto(self):
        """Prueba si la manivela gira correctamente devuelve True"""
        maquina = MaquinaBolas()
        giro = 360
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp, True)

    def test_giro_manivela_incorrecto(self):
        """Prueba si la manivela gira incorrectamente devuelve False"""
        maquina = MaquinaBolas()
        giro = 30
        resp = maquina.girar_manivela(giro)
        self.assertEqual(resp, False)

#    def test_moneda_y_giro_correctos_suelta_bola(self):
#       """Si las condiciones son correctas suelta una bola"""
#        maquina = MaquinaBolas()
#        resp = maquina.soltar_bola()
#        self.assertEqual(resp,BOLA)

    def test_moneda_y_giro_correctos_suelta_bola(self):
        """ Si las condiciones son correctas suelta una bola"""
        maquina = MaquinaBolas()
        dep = maquina.deposito
        mon = maquina.monedero
        resp = maquina.soltar_bola()

        self.assertEqual(resp, BOLA)
        self.assertEqual(maquina.deposito, dep-1)
        self.assertEqual(maquina.monedero, mon+1)
