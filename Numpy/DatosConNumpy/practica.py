
import numpy as np

# Función para generar datos de ventas aleatorias
def generar_datos_ventas(productos, tiendas, dias):
    """
    Genera un array de ventas aleatorias de productos en tiendas durante varios días.

    Parámetros:
    productos (int): Número de productos.
    tiendas (int): Número de tiendas.
    dias (int): Número de días.

    Retorna:
    numpy.ndarray: Array 3D con los datos de ventas.
    """
    return np.random.randint(0, 100, size=(productos, tiendas, dias))

# Función para calcular el total de ventas por producto durante la semana
def total_ventas_por_producto(ventas):
    """
    Calcula el total de ventas por cada producto durante la semana.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    numpy.ndarray: Array 1D con el total de ventas por producto.
    """
    return np.sum(ventas, axis=(1, 2))

# Función para calcular el total de ventas por tienda durante la semana
def total_ventas_por_tienda(ventas):
    """
    Calcula el total de ventas por cada tienda durante la semana.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    numpy.ndarray: Array 1D con el total de ventas por tienda.
    """
    return np.sum(ventas, axis=(0, 2))

# Función para calcular el promedio de ventas por producto por día
def promedio_ventas_por_producto(ventas):
    """
    Calcula el promedio de ventas por cada producto por día.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    numpy.ndarray: Array 1D con el promedio de ventas por producto por día.
    """
    return np.mean(ventas, axis=(1, 2))

# Función para calcular el promedio de ventas por tienda por día
def promedio_ventas_por_tienda(ventas):
    """
    Calcula el promedio de ventas por cada tienda por día.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    numpy.ndarray: Array 1D con el promedio de ventas por tienda por día.
    """
    return np.mean(ventas, axis=(0, 2))

# Función para encontrar el producto con mayor y menor ventas totales en la semana
def producto_mayor_menor_ventas(ventas):
    """
    Encuentra el producto con mayor y menor ventas totales en la semana.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    tuple: Índices del producto con mayor y menor ventas.
    """
    total_por_producto = total_ventas_por_producto(ventas)
    return np.argmax(total_por_producto), np.argmin(total_por_producto)

# Función para encontrar la tienda con mayor y menor ventas totales en la semana
def tienda_mayor_menor_ventas(ventas):
    """
    Encuentra la tienda con mayor y menor ventas totales en la semana.

    Parámetros:
    ventas (numpy.ndarray): Array 3D con los datos de ventas.

    Retorna:
    tuple: Índices de la tienda con mayor y menor ventas.
    """
    total_por_tienda = total_ventas_por_tienda(ventas)
    return np.argmax(total_por_tienda), np.argmin(total_por_tienda)

# Programa principal

# Generar datos de ventas
productos = 10
tiendas = 5
dias = 7
ventas = generar_datos_ventas(productos, tiendas, dias)

# Calcular totales y promedios
total_producto = total_ventas_por_producto(ventas)
total_tienda = total_ventas_por_tienda(ventas)
promedio_producto = promedio_ventas_por_producto(ventas)
promedio_tienda = promedio_ventas_por_tienda(ventas)
producto_max, producto_min = producto_mayor_menor_ventas(ventas)
tienda_max, tienda_min = tienda_mayor_menor_ventas(ventas)

# Mostrar resultados
print("Total de ventas por producto durante la semana:", total_producto)
print("Total de ventas por tienda durante la semana:", total_tienda)
print("Promedio de ventas por producto por día:", promedio_producto)
print("Promedio de ventas por tienda por día:", promedio_tienda)
print(f"Producto con mayores ventas totales en la semana: Producto {producto_max}")
print(f"Producto con menores ventas totales en la semana: Producto {producto_min}")
print(f"Tienda con mayores ventas totales en la semana: Tienda {tienda_max}")
print(f"Tienda con menores ventas totales en la semana: Tienda {tienda_min}")
datos = generar_datos_ventas(10,5,7)
print(datos.shape)