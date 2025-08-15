import pandas as pd
import plotly.express as px

# Cargar dataset diario (ruta relativa desde la carpeta notebooks)
df = pd.read_csv("../data/pm25_90d_daily.csv", parse_dates=["date"])

# Comprobar que tiene las columnas necesarias
required_cols = {"city", "date", "pm25", "lat", "lon"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"Faltan columnas requeridas: {required_cols - set(df.columns)}")

# Mapa interactivo de contaminación PM2.5 promedio por ciudad
avg_city = df.groupby(["city", "lat", "lon"], as_index=False)["pm25"].mean()
fig_map = px.scatter_mapbox(
    avg_city,
    lat="lat",
    lon="lon",
    size="pm25",
    color="pm25",
    color_continuous_scale="RdYlGn_r",
    size_max=30,
    zoom=3,
    mapbox_style="open-street-map",
    title="Promedio PM2.5 por ciudad (últimos 90 días)"
)
fig_map.show()

# Línea temporal de PM2.5 por ciudad
fig_line = px.line(
    df,
    x="date",
    y="pm25",
    color="city",
    title="Evolución diaria de PM2.5 por ciudad",
    labels={"pm25": "PM2.5 (µg/m³)", "date": "Fecha"}
)

# Banda de seguridad de la OMS (PM2.5 ≤ 15 µg/m³)
fig_line.add_hrect(y0=0, y1=15, fillcolor="green", opacity=0.1, line_width=0)

fig_line.show()
