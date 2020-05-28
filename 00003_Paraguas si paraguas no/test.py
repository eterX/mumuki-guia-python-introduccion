import sys,unittest
sys.path.append(".")
from extra import clima
paraguas_si_paraguas_no = clima.paraguas_si_paraguas_no #esto lo hago para probar las pruebas, no se si es necesario


class Test(unittest.TestCase):

  def test_paraguas_si_paraguas_no_base(self, llueve = True, hace_frío = True, resultado = True):
    self.assertEquals(paraguas_si_paraguas_no(llueve,hace_frío), resultado)


  def test_paraguas_si_paraguas_no_combinaciones(self):
    miClima = clima()
    for testBase in miClima.combinaciones():
      self.assertEquals(paraguas_si_paraguas_no(**testBase["args"]), testBase["resultado"])


  def test_true(self):
    self.assertTrue(True)



