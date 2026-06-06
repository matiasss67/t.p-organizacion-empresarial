import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
ventas = pd.read_csv("../datos/ventas.csv")

# Convertir fecha
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Calcular monto total por venta
ventas["total"] = ventas["cantidad"] * ventas["precio"]

# Ventas totales
ventas_totales = ventas["total"].sum()

# Producto más vendido
producto_mas_vendido = (
    ventas.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

# Ventas por mes
ventas["mes"] = ventas["fecha"].dt.to_period("M")

ventas_mes = (
    ventas.groupby("mes")["total"]
    .sum()
)

print("VENTAS TOTALES:", ventas_totales)
print("PRODUCTO MAS VENDIDO:", producto_mas_vendido)

# Guardar resumen
resumen = pd.DataFrame({
    "ventas_totales":[ventas_totales],
    "producto_mas_vendido":[producto_mas_vendido]
})

resumen.to_csv(
    "../resultados/resumen_ventas.csv",
    index=False
)

# Gráfico
ventas_mes.plot(kind="line")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto")

plt.tight_layout()

plt.savefig(
    "../resultados/grafico_ventas.png"
)

print("Proceso finalizado.")