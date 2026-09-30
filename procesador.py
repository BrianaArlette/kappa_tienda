from collections import Counter

class ProcesadorVentas:
    def __init__(self):
        self.eventos_procesados = 0
        self.productos_vendidos = 0
        self.ingresos_totales = 0
        self.ventas_por_producto = Counter()
        self.metodos_pago = Counter()
        self.historial_ingresos = []

    def procesar_compra(self, compra):
        self.eventos_procesados += 1
        self.ingresos_totales += compra["total"]

        for producto in compra["productos"]:
            nombre = producto["producto"]
            cantidad = producto["cantidad"]

            self.productos_vendidos += cantidad
            self.ventas_por_producto[nombre] += cantidad

        self.metodos_pago[compra["metodo_pago"]] += 1

        self.historial_ingresos.append(self.ingresos_totales)

    def obtener_producto_mas_vendido(self):
        if not self.ventas_por_producto:
            return "Sin ventas", 0

        producto, cantidad = self.ventas_por_producto.most_common(1)[0]

        return producto, cantidad

    def obtener_promedio_compra(self):
        if self.eventos_procesados == 0:
            return 0

        return self.ingresos_totales / self.eventos_procesados

    def mostrar_estadisticas(self):
        producto_mas_vendido, cantidad = self.obtener_producto_mas_vendido()

        print("\n========== ESTADISTICAS ==========")
        print(f"Eventos procesados: {self.eventos_procesados}")
        print(f"Productos vendidos: {self.productos_vendidos}")
        print(f"Ingresos totales: ${self.ingresos_totales:,.2f}")
        print(
            f"Promedio por compra: "
            f"${self.obtener_promedio_compra():,.2f}"
        )
        print(
            f"Producto mas vendido: "
            f"{producto_mas_vendido} ({cantidad} unidades)"
        )

        print("\nVentas por producto:")

        for producto, cantidad in self.ventas_por_producto.items():
            print(f"- {producto}: {cantidad}")

        print("\nMetodos de pago:")

        for metodo, cantidad in self.metodos_pago.items():
            print(f"- {metodo}: {cantidad}")

        print("==================================")
