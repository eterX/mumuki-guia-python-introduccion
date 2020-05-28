class clima():
  def __init__(self):
    self.llueve = True
    self.hace_frío = True

  def paraguas_si_paraguas_no(self, llueve, hace_frío):
    """
       funcion patrón para el ejercicio3
    """
    resultado = llueve and hace_frío
    return resultado

  def combinaciones(self):
    resultado = list()
    for llueve in [True, False]:
      for hace_frío in [True, False]:
        args=dict(llueve=llueve,hace_frío=hace_frío)
        salida=self.paraguas_si_paraguas_no(**args)
        resultado.append((args,salida))
    return resultado

