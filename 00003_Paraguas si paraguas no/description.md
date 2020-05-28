# Paraguas si, paraguas no

Este ejercicio se llama "Paraguas si, paraguas no" pero si fuera una peli se llamaría "A todo o nada" :)   
Cuantas veces tomamos decisiones entre dos opciones? Muchííísimas:

- subir por escalera o por ascensor 
- se nos cae la tostada, con el dulce par arriba :smile: o para abajo :shroud:
- atajamos entre los palos o salimos? (a cortar la jugada)
- llevamos paraguas o no lo llevamos?

En nuestros programas esas decisiones dependenden de una variable que llamamos "variable Lógica" (o también "Booleana"). Y  resultado de expresiones Lógicas. Por ejemplo, las sigiuentes expresiones lógicas nos indican si salimos con paraguas:

- tengo_paraguas **Y** **NO** presté_paraguas 
- paraguas_funciona **Y** ( en_su_lugar **O** en_puerta)
- llueve **O** hace_frío 

La siguiente función nos hace llevar paraguas según la última expresión anterior:
```python
def paraguas_si_paraguas_no(llueve,hace_frío):
    """
    este programa es para gente fríolenta: te dice si salir con paraguas (devuelve un valor booleano) y será verdadero (True) si llueve o hace_frío son verdaderos  
    """
    resultado = llueve or hace_frío
    return resultado
```

Realice un programa (parecido al ejemplo), para gente *no tan* friolenta: te dice si salir con paraguas (devuelve un valor booleano) y será falso  (False) si llueve o hace_frío son falsos. 
En otras palabras: tienen que ser verdaderas ambas entradas llueve y hace_frío para que esa gente corajuda salga con paraguas.


### ayuda

<p style="{color: orangered;}">
Como Python trata de parecerse al lenguaje natural Inglés, sus operadores lógicos también se parecen:
<table>
<tr><td>En castellano</td><td>En Inglés</td><td>Ejemplo Python</td></tr>
<tr><td>Negación (no)</td><td>not</td><td>resultado = <b>not(</b>llueve<b>)</b></td></tr>
<tr><td>Disyunción (o)</td><td>or</td><td>resultado = llueve <b>or</b> hace_frío</td></tr>
<tr><td>Conjunción (y)</td><td>and</td><td>resultado = llueve <b>and</b> hace_frío</td></tr>
<tr><td>Equivalencia</td><td> ?</td><td>resultado =  (llueve <b>==</b> hace_frío)</td></tr>
</table>
<p>


