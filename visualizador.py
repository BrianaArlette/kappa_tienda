import matplotlib.pyplot as plt


class VisualizadorVentas:
    def __init__(self):
        plt.ion()

        self.figura, (self.grafica_productos, self.grafica_ingresos) = (
            plt.subplots(1, 2, figsize=(12, 5))
        )

        self.figura.suptitle("Ventas en tiempo real")

    def actualizar(self, procesador):
        self.grafica_productos.clear()
        self.grafica_ingresos.clear()

        # Grafica 1: productos vendidos
        productos = list(procesador.ventas_por_producto.keys())
        cantidades = list(procesador.ventas_por_producto.values())

        self.grafica_productos.bar(
            productos,
            cantidades
        )

        self.grafica_productos.set_title(
            "Productos vendidos"
        )

        self.grafica_productos.set_xlabel(
            "Producto"
        )

        self.grafica_productos.set_ylabel(
            "Unidades vendidas"
        )

        # Grafica 2: ingresos acumulados
        eventos = range(
            1,
            len(procesador.historial_ingresos) + 1
        )

        self.grafica_ingresos.plot(
            eventos,
            procesador.historial_ingresos,
            marker="o"
        )

        self.grafica_ingresos.set_title(
            "Ingresos acumulados"
        )

        self.grafica_ingresos.set_xlabel(
            "Eventos procesados"
        )

        self.grafica_ingresos.set_ylabel(
            "Ingresos"
        )

        self.figura.tight_layout()

        plt.pause(0.01)