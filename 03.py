class Carril:
    def __init__(self):
        self.cola = deque()

class Semaforo:
    def __init__(self):
        self.estado = "NS_VERDE"

    def siguiente_estado(self):
        self.estado = "EW_VERDE" if self.estado == "NS_VERDE" else "NS_VERDE"
