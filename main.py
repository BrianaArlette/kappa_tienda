import threading
import time
import socket
import json

from queue import Queue

from productor import (
    generar_compra,
    generar_compra_manual,
    mostrar_compra
)

from procesador import ProcesadorVentas
from visualizador import VisualizadorVentas
from registro import guardar_evento


HOST = "127.0.0.1"
PORT = 5050

cola_eventos = Queue()
sistema_activo = True


def productor_automatico():
    global sistema_activo

    while sistema_activo:
        compra = generar_compra()

        cola_eventos.put(compra)

        time.sleep(5) 


def servidor_compras_manuales():
    global sistema_activo

    with socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    ) as servidor:

        servidor.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        servidor.bind((HOST, PORT))
        servidor.listen()
        servidor.settimeout(0.5)

        while sistema_activo:

            try:
                conexion, direccion = servidor.accept()

            except socket.timeout:
                continue

            with conexion:

                try:
                    datos = conexion.recv(4096)

                    solicitud = json.loads(
                        datos.decode("utf-8")
                    )

                    compra = generar_compra_manual(
                        solicitud["producto"],
                        solicitud["cantidad"],
                        solicitud["metodo_pago"]
                    )

                    cola_eventos.put(compra)

                    respuesta = {
                        "ok": True,
                        "cliente": compra["cliente"],
                        "id_evento": compra["id_evento"]
                    }

                except Exception as error:

                    respuesta = {
                        "ok": False,
                        "error": str(error)
                    }

                conexion.sendall(
                    json.dumps(respuesta).encode("utf-8")
                )


def main():
    global sistema_activo

    procesador = ProcesadorVentas()
    visualizador = VisualizadorVentas()

    print("==========================================")
    print("     SISTEMA DE VENTAS EN TIEMPO REAL")
    print("==========================================")
    print("Esperando eventos...")
    print("Ctrl + C para detener.\n")

    hilo_automatico = threading.Thread(
        target=productor_automatico,
        daemon=True
    )

    hilo_manual = threading.Thread(
        target=servidor_compras_manuales,
        daemon=True
    )

    hilo_automatico.start()
    hilo_manual.start()

    try:

        while sistema_activo:

            if not cola_eventos.empty():

                compra = cola_eventos.get()

                mostrar_compra(compra)

                guardar_evento(compra)

                procesador.procesar_compra(compra)

                procesador.mostrar_estadisticas()

                visualizador.actualizar(
                    procesador
                )

            time.sleep(0.1)

    except KeyboardInterrupt:
        sistema_activo = False

    print("\n==========================================")
    print("              SISTEMA DETENIDO")
    print("==========================================")


if __name__ == "__main__":
    main()