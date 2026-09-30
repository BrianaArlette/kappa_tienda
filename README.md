# Simulación de Arquitectura Kappa - Tienda en línea

## Descripción

Este proyecto simula el procesamiento continuo de eventos de una tienda en línea utilizando Python, con el objetivo de representar los principios básicos de la Arquitectura Kappa.

Cada compra se considera un evento que se procesa conforme llega. El sistema genera compras automáticas de forma continua y también permite ingresar compras manuales desde una segunda terminal. Ambos tipos de eventos son procesados por el mismo sistema.

A partir de estos eventos se actualizan estadísticas y gráficas en tiempo real, además de conservar un registro histórico de las compras.

## Funcionalidades

- Generación automática de compras.
- Generación de compras manuales.
- Clientes numerados de manera consecutiva.
- Procesamiento continuo de eventos.
- Registro de compras automáticas y manuales.
- Actualización de estadísticas en tiempo real.
- Visualización de productos vendidos.
- Visualización de ingresos acumulados.
- Almacenamiento local del historial de eventos.

Cada compra contiene información como:

- ID del evento.
- Cliente.
- Productos y cantidades.
- Precios y subtotal.
- Descuento.
- Total de la compra.
- Método de pago.
- Fecha y hora.
- Tipo de evento: `AUTOMATICA` o `MANUAL`.

## Estadísticas procesadas

El sistema actualiza continuamente:

- Eventos procesados.
- Productos vendidos.
- Ingresos totales.
- Promedio por compra.
- Producto más vendido.
- Ventas por producto.
- Métodos de pago utilizados.

## Estructura del proyecto

### `main.py`
Archivo principal. Inicia la generación automática de eventos, recibe las compras manuales y coordina su procesamiento, registro y visualización.

### `productor.py`
Contiene la lógica para generar las compras y sus datos.

### `procesador.py`
Procesa cada compra y mantiene actualizadas las estadísticas.

### `compra_manual.py`
Permite generar una compra desde una segunda terminal seleccionando producto, cantidad y método de pago.

### `visualizador.py`
Genera las gráficas de productos vendidos e ingresos acumulados y las actualiza conforme llegan nuevos eventos.

### `registro.py`
Guarda los eventos procesados en `eventos.jsonl`.

El archivo `eventos.jsonl` se genera automáticamente durante la ejecución y no se incluye en el repositorio.

### `requirements.txt`
Contiene las dependencias necesarias para ejecutar el proyecto.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/BrianaArlette/kappa_tienda.git
```

Entrar a la carpeta:

```bash
cd kappa_tienda
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

En la primera terminal ejecutar:

```bash
python main.py
```

Esto inicia la generación automática de compras, el procesamiento de eventos, las estadísticas y las gráficas en tiempo real.

Para realizar una compra manual, abrir una segunda terminal y ejecutar:

```bash
python compra_manual.py
```

Desde esta terminal se selecciona el producto, la cantidad y el método de pago. La compra se envía al proceso principal y se incorpora al mismo flujo que las compras automáticas.

Para detener el sistema principal:

```text
Ctrl + C
```

## Relación con Arquitectura Kappa

La práctica representa un sistema orientado a eventos en el que la información se procesa conforme se genera. Las compras funcionan como eventos dentro de un flujo continuo y son procesadas mediante una misma lógica, independientemente de si fueron generadas automática o manualmente.

De esta forma se puede observar de manera práctica cómo un flujo de datos puede producir resultados y visualizaciones actualizadas continuamente.