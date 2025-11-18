#Implementa aquí todos los procesos necesarios para la operación de eliminación. 
#Pueden modificar la extensión del documento para que se ajuste al lenguaje de su elección y comentar estas instrucciones.

class NodoArbolB:
    
    def __init__(self, t, hoja=False):
        self.t = t
        self.hoja = hoja  
        self.keys = []  # Llaves almacenadas
        self.hijos = []  # Hijos del nodo

    def delete(self, k):
        t = self.t
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == k:
            if self.hoja:
                # simplemente se elimina
                self.keys.pop(i)
            else:
                if len(self.hijos[i].keys) >= t:
                    pred = self.obtener_predecesor(i)
                    self.keys[i] = pred
                    self.hijos[i].delete(pred)
                elif len(self.hijos[i + 1].keys) >= t:
                    succ = self.obtener_sucesor(i)
                    self.keys[i] = succ
                    self.hijos[i + 1].delete(succ)
                else:
                    self.fusionar(i)
                    self.hijos[i].delete(k)
        else:
            if self.hoja:
                print(f"El valor {k} no está en el árbol.")
                return
            # Se asegura que el hijo tenga al menos t llaves
            if len(self.hijos[i].keys) < t:
                self.rellenar(i)
            self.hijos[i].delete(k)

    def obtener_predecesor(self, i):
        curr = self.hijos[i]
        while not curr.hoja:
            curr = curr.hijos[-1]
        return curr.keys[-1]

    def obtener_sucesor(self, i):
        curr = self.hijos[i + 1]
        while not curr.hoja:
            curr = curr.hijos[0]
        return curr.keys[0]

    def fusionar(self, i):
        hijo1 = self.hijos[i]
        hijo2 = self.hijos[i + 1]
        hijo1.keys.append(self.keys.pop(i))
        hijo1.keys.extend(hijo2.keys)
        if not hijo1.hoja:
            hijo1.hijos.extend(hijo2.hijos)
        self.hijos.pop(i + 1)

    def rellenar(self, i):
        if i > 0 and len(self.hijos[i - 1].keys) >= self.t:
            self.pedir_del_anterior(i)
        elif i < len(self.keys) and len(self.hijos[i + 1].keys) >= self.t:
            self.pedir_del_siguiente(i)
        else:
            if i < len(self.keys):
                self.fusionar(i)
            else:
                self.fusionar(i - 1)

    def pedir_del_anterior(self, i):
        hijo = self.hijos[i]
        hermano = self.hijos[i - 1]
        hijo.keys.insert(0, self.keys[i - 1])
        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())
        self.keys[i - 1] = hermano.keys.pop()

    def pedir_del_siguiente(self, i):
        hijo = self.hijos[i]
        hermano = self.hijos[i + 1]
        hijo.keys.append(self.keys[i])
        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))
        self.keys[i] = hermano.keys.pop(0)


class ArbolB:
    
    def __init__(self, t):
        self.t = t
        self.raiz = NodoArbolB(t, True)

    def delete(self, k):
        self.raiz.delete(k)
        if not self.raiz.keys and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]

    def recorrer(self):
        self._recorrer(self.raiz)

    def _recorrer(self, nodo):
        for i in range(len(nodo.keys)):
            if not nodo.hoja:
                self._recorrer(nodo.hijos[i])
            print(nodo.keys[i], end=" ")
        if not nodo.hoja:
            self._recorrer(nodo.hijos[-1])
        print()
