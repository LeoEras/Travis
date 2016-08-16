import unittest
from programa import *

class SimpleTestCase(unittest.TestCase):
    def testA(self):
        libro = Libro("CE", 0)
        assert libro.prestamo("10/02/2015") == "17/02/2015"

    def testB(self):
        libro = Libro("CH", 0)
        assert libro.prestamo("10/02/2015") == "24/02/2015"

    def testC(self):
        libro = Libro("CE", 1)
        assert libro.prestamo("10/02/2015") == 0

    def testD(self):
        libro = Libro("CN", 1)
        assert libro.prestamo("10/02/2015") == 0

    def testE(self):
        libro = Libro("AD", 1)
        assert libro.prestamo("10/02/2015") == None
        
if __name__ == "__main__":
    unittest.main()
