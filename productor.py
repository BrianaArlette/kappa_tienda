import random
import uuid
import time
from datetime import datetime


productos = {
    "Mouse": 500,
    "Audifonos": 800,
    "Webcam": 900,
    "Teclado": 1200,
    "Monitor": 3500
}

metodos_pago = [
    "Tarjeta",
    "Transferencia",
    "Apple Pay",
    "Efectivo"
]

contador_cliente = 1


def siguiente_cliente():
    global contador_cliente

    cliente = f"Cliente_{contador_cliente}"
    contador_cliente += 1

    return cliente


def generar_productos_compra():
    cantidad_productos = random.randint(1, 3)

    productos_elegidos = random.sample(
        list(productos.keys()),
        cantidad_productos
    )

    carrito = []

    for producto in productos_elegidos:
        precio = productos[producto]
        cantidad = random.randint(1, 3)
        subtotal = precio * cantidad

        carrito.append({
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

    return carrito


def generar_compra():
    carrito = generar_productos_compra()

    subtotal_compra = sum(
        producto["subtotal"]
        for producto in carrito
    )

    descuento = random.choice([0, 0, 0, 0.05, 0.10])

    monto_descuento = subtotal_compra * descuento
    total = subtotal_compra - monto_descuento

    compra = {
        "id_evento": str(uuid.uuid4())[:8],
        "cliente": siguiente_cliente(),
        "productos": carrito,
        "metodo_pago": random.choice(metodos_pago),
        "subtotal": subtotal_compra,
        "descuento": descuento,
        "total": round(total, 2),
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "tipo": "AUTOMATICA"
    }

    return compra


def mostrar_compra(compra):
    print("\n========== NUEVO EVENTO ==========")

    print(f"ID: {compra['id_evento']}")
    print(f"Cliente: {compra['cliente']}")
    print(f"Fecha: {compra['fecha']}")
    print(f"Hora: {compra['hora']}")

    print("\nProductos:")

    for producto in compra["productos"]:
        print(
            f"- {producto['producto']} | "
            f"${producto['precio']} | "
            f"x{producto['cantidad']} | "
            f"${producto['subtotal']}"
        )

    print(f"\nSubtotal: ${compra['subtotal']}")
    print(f"Descuento: {compra['descuento'] * 100:.0f}%")
    print(f"Total: ${compra['total']}")
    print(f"Método de pago: {compra['metodo_pago']}")
    print(f"Tipo: {compra['tipo']}")

    print("==================================")


def flujo_compras(intervalo=2):
    while True:
        compra = generar_compra()
        yield compra
        time.sleep(intervalo)


if __name__ == "__main__":
    print("STREAM DE COMPRAS INICIADO")
    print("Presiona Ctrl + C para detenerlo.\n")

    try:
        for compra in flujo_compras():
            mostrar_compra(compra)

    except KeyboardInterrupt:
        print("\nStream detenido.")