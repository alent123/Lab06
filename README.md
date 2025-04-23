# 🧪 Lab06: Estructuras de Cola Circular - Algoritmos y Estructuras de Datos

Este repositorio contiene la solución completa al laboratorio de la semana 6, basado en la implementación y aplicación de **colas circulares** mediante distintos retos prácticos.

## 👨‍🎓 Integrantes del equipo

- **GARCIA CCENCHO, CRISTIAN RUFINO**
- **SALAS PEREZ, SANTIAGO AGUSTIN**
- **BELLIDO CHAMBI, RONY WIDMER**

**Curso:** Algoritmos y Estructuras de Datos  
**Docente:** Garamendi Sarmiento, Elliot Leo

---

## 📚 Descripción del Proyecto

El laboratorio incluye 5 retos técnicos, todos enfocados en aplicar estructuras de **colas circulares** y derivadas (como `deque`) a problemas reales de programación y simulación.

Cada miembro del equipo desarrolló un reto distinto según lo indicado en el enunciado del laboratorio.

---

## 📌 Retos Desarrollados

### 🔹 Reto 1: Sliding Window Maximum
- **Problema:** Encontrar el máximo en cada subarreglo de tamaño `k`.
- **Solución:** Uso de `deque` para mantener solo los índices relevantes y lograr eficiencia `O(n)`.

### 🔹 Reto 2: Rotación de Arreglo
- **Problema:** Rotar el arreglo `k` posiciones a la derecha.
- **Solución:** Inversión de segmentos del arreglo para realizar rotación in-place.

### 🔹 Reto 3: Simulación de Semáforo
- **Problema:** Controlar tráfico usando colas circulares para representar carriles.
- **Solución:** Alternancia de luces con `toggle()` y FIFO para paso de vehículos.

### 🔹 Reto 4: Planificador Round-Robin
- **Problema:** Simular asignación de CPU a procesos.
- **Solución:** Cola circular que asigna tiempo a cada proceso hasta que terminen.

### 🔹 Reto 5: Buffer Circular de Datos
- **Problema:** Conservar los últimos `N` datos de un flujo.
- **Solución:** Arreglo circular que sobrescribe los datos más antiguos cuando se llena.
