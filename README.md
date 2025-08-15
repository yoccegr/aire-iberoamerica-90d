
# Análisis de Calidad del Aire - PM2.5

Este proyecto analiza los niveles de **PM2.5** en distintas ciudades, comparándolos con el límite recomendado por la **Organización Mundial de la Salud (OMS)**.

## 📊 Visualizaciones

### 1️⃣ Evolución diaria de PM2.5 por ciudad
Muestra la tendencia diaria de las concentraciones de PM2.5 en cada ciudad durante el período de estudio.

![Evolución diaria PM2.5](images/lineas_pm25.png)

### 2️⃣ Comparación directa entre ciudades
Gráfico de líneas que permite comparar en la misma escala los valores de PM2.5 entre las ciudades seleccionadas.

![Comparación directa](images/comparacion_ciudades.png)

### 3️⃣ Porcentaje de días sobre el límite OMS
Gráfico de barras que indica el porcentaje de días en que cada ciudad superó el límite recomendado por la OMS.

![Porcentaje sobre OMS](images/barras_pct_sobre_oms.png)

## 📄 Metodología

1. **Carga de datos**: Se procesan los registros de PM2.5 por fecha y ciudad.
2. **Cálculo de días sobre OMS**: Se marca cada día en que el valor excede el límite de 15 μg/m³.
3. **Visualización**: Se generan gráficos comparativos y de resumen.
4. **Interpretación**: Se observan patrones y se identifican las ciudades más críticas.

## 🛠️ Tecnologías utilizadas

- **Python** (pandas, plotly)
- **Jupyter Notebook**
- **Git/GitHub** para control de versiones

## 📌 Resultados clave

- Santiago presenta la mayor variabilidad y los niveles más altos de PM2.5.
- Ciudad de México y Madrid mantienen niveles moderados pero con picos significativos.
- Río de Janeiro muestra niveles bajos durante el período analizado.

---
📬 *Autor*: Yocce González  
📅 *Última actualización*: Agosto 2025
