from collections import deque

def planificador_round_robin(procesos, quantum):
    cola = deque(procesos)
    tiempo = 0
    while cola:
        p = cola.popleft()
        tiempo_ejecucion = min(p['restante'], quantum)
        tiempo += tiempo_ejecucion
        p['restante'] -= tiempo_ejecucion
        if p['restante'] > 0:
            cola.append(p)
