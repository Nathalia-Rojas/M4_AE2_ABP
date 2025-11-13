# 💳 Proyecto: Clase TarjetaCredito (Programación Orientada a Objetos en Python)

## 🧠 Descripción

Este proyecto implementa una clase llamada **`TarjetaCredito`**, como parte de una práctica de **programación orientada a objetos (POO)**.  
El objetivo es simular el comportamiento de una tarjeta de crédito: permitir compras, pagos, aplicación de intereses y mostrar la información actual del saldo.

También se incluyen conceptos importantes como:
- Uso de **atributos** y **métodos de instancia**.
- Implementación de **valores por defecto** en el constructor.
- Encadenamiento de métodos (method chaining).
- Creación de un **método de clase** para mostrar todas las instancias creadas.

---

## 🧩 Objetivos de la práctica

1. Practicar las convenciones para crear clases.
2. Implementar argumentos por defecto.
3. Usar estructuras de control dentro de los métodos.
4. Crear y actualizar atributos mediante `self`.
5. Probar las funcionalidades a través de la creación de instancias e invocación de métodos.
6. Encadenar métodos para realizar varias operaciones en una sola línea.
7. BONUS: crear un método de clase para mostrar todas las tarjetas registradas.

---

## 🏗️ Estructura de la clase

La clase **`TarjetaCredito`** tiene los siguientes atributos y métodos:

### **Atributos**
- `saldo_pagar`: Monto actual a pagar (por defecto `0`).
- `limite_credito`: Límite máximo de crédito permitido.
- `intereses`: Porcentaje de interés mensual expresado como decimal (ej. `0.02` para 2%).
- `tarjetas`: Lista de clase que guarda todas las instancias creadas.

### **Métodos**
- `__init__(self, limite_credito, intereses, saldo_pagar=0)`: Constructor con valores por defecto.
- `compra(self, monto)`: Aumenta el saldo si no se supera el límite de crédito.
- `pago(self, monto)`: Disminuye el saldo a pagar.
- `cobrar_interes(self)`: Aplica intereses al saldo actual.
- `mostrar_info_tarjeta(self)`: Muestra el saldo actual.
- `mostrar_todas(cls)`: Método de clase para mostrar la información de todas las tarjetas creadas.

---

## 💻 Ejemplo de uso

```python
# Crear tres tarjetas
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.03)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.05)

# Primera tarjeta: 2 compras, 1 pago, cobrar interés y mostrar info
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 3 compras, 2 pagos, cobrar interés y mostrar info
tarjeta2.compra(500).compra(700).compra(200).pago(300).pago(200).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta: 5 compras (una excede el límite) y mostrar info
tarjeta3.compra(100).compra(150).compra(100).compra(120).compra(80).mostrar_info_tarjeta()

# BONUS: Mostrar todas las tarjetas creadas
TarjetaCredito.mostrar_todas()