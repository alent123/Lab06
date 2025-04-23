class BufferCircular:
    def __init__(self, tamaño):
        self.buffer = [None]*tamaño
        self.tamaño = tamaño
        self.indice = 0
        self.contador = 0

    def agregar(self, valor):
        self.buffer[self.indice] = valor
        self.indice = (self.indice + 1) % self.tamaño
        self.contador = min(self.contador + 1, self.tamaño)

    def obtener_recientes(self):
        if self.contador < self.tamaño:
            return self.buffer[:self.indice]
        return self.buffer[self.indice:] + self.buffer[:self.indice]
