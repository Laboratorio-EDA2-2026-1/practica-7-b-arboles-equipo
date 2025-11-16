#Implementa aquí la operación de búsqueda. 
#Pueden modificar la extensión del documento para que se ajuste al lenguaje de su elección y comentar estas #instrucciones.

class NodoB:
    def __init__(self, t, hoja=False):
        self.t = t
        self.claves = []
        self.hijos = []
        self.hoja = hoja
    
    def num_claves(self):
        return len(self.claves)

def Busqueda(x, k):
    i = 0
    while i < len(x.claves) and k > x.claves[i]:
        i += 1

    if i < len(x.claves) and k == x.claves[i]:
        return (x, i)

    if x.hoja:
        return None
    
    return Busqueda(x.hijos[i], k)


