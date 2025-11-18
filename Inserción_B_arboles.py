class BTree:
    def __init__(self, t):
        self.raiz = BTreeNode(t, True)
        self.t = t  # Grado mínimo
    
    def insert(self, k):
        #inserción de una clave
        root = self.raiz
        
        # Si la raíz está llena, dividirla
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t, False)
            self.raiz = temp
            temp.hijo.insert(0, root)
            self.dividir_hijo(temp, 0)
            self.insertar_no_lleno(temp, k)
        else:
            self.insertar_no_lleno(root, k)
    
    def insertar_no_lleno(self, x, k):
        i = len(x.keys) - 1
        
        if x.hoja:
            # insertamos en nodo hoja
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            #encontramos el nodo adecuaco
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            
            # dividimos
            if len(x.hijo[i].keys) == (2 * self.t) - 1:
                self.dividir_hijo(x, i)
                if k > x.keys[i]:
                    i += 1
            
            self.insertar_no_lleno(x.hijo[i], k)
    
    def dividir_hijo(self, x, i):
        t = self.t
        y = x.hijo[i]
        z = BTreeNode(t, y.hoja)
        

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        

        if not y.hoja:
            z.hijo = y.hijo[t:(2 * t)]
            y.hijo = y.hijo[0:t]
        
        x.hijo.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        y.keys = y.keys[0:(t - 1)]
