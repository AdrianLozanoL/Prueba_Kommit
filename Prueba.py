class pila:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.previo = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

#Insert head and tail

    def insertar_cabeza(self,data):
        nuevo_nodo = pila(data)
        #En caso de que la lista este vacio se hace uso del condicional 
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = pila(data)
            self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo

#Remove an element


#Remove all repeated elements


#Search for an element, returning it's index if found


#Size of the list
