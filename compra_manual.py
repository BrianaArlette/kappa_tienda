import socket
import json

from productor import productos, metodos_pago


HOST = "127.0.0.1"
PORT = 5050


def realizar_compra_manual():
    lista_productos = list(productos.keys())

    print("\n========== COMPRA MANUAL ==========")

    for numero, producto in enumerate(lista_productos, start=1):
        print(f"{numero}. {producto} - ${productos[producto]}")

    try:
        seleccion = int(input("\nSelecciona un producto: "))
        producto = lista_productos[seleccion - 1]

        cantidad = int(input("Cantidad: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        print("\n========== METODOS DE PAGO ==========")

        for numero, metodo in enumerate(metodos_pago, start=1):
            print(f"{numero}. {metodo}")

        seleccion_pago = int(
            input("\nSelecciona método de pago: ")
        )

        metodo_pago = metodos_pago[seleccion_pago - 1]

        solicitud = {
            "producto": producto,
            "cantidad": cantidad,
            "metodo_pago": metodo_pago
        }

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PORT))

            cliente.sendall(
                json.dumps(solicitud).encode("utf-8")
            )

            respuesta = cliente.recv(4096)

        respuesta = json.loads(
            respuesta.decode("utf-8")
        )

        if respuesta["ok"]:
            print("\nCompra enviada al stream")
            print(f"Cliente: {respuesta['cliente']}")
            print(f"ID evento: {respuesta['id_evento']}")

        else:
            print("\nError:", respuesta["error"])

    except (ValueError, IndexError):
        print("\nOpción inválida.")

    except ConnectionRefusedError:
        print(
            "\nNo se pudo conectar."
            "\nPrimero ejecuta main.py."
        )


if __name__ == "__main__":
    realizar_compra_manual()