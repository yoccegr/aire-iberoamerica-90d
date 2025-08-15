
# Análisis de Calidad del Aire — PM2.5 en Ciudades Iberoamericanas

## Introducción
Este proyecto tiene como objetivo analizar la calidad del aire en distintas ciudades de Iberoamérica, enfocándose en el contaminante PM2.5. El PM2.5 corresponde a partículas finas de diámetro menor o igual a 2,5 micrómetros, capaces de penetrar profundamente en los pulmones y representar un riesgo significativo para la salud.  
La Organización Mundial de la Salud (OMS) recomienda que la concentración diaria de PM2.5 no supere los **15 µg/m³**.

## Fuente de Información
Los datos utilizados provienen de [OpenAQ](https://openaq.org), una plataforma de acceso libre que recopila mediciones de calidad del aire de estaciones oficiales y redes ciudadanas a nivel mundial.

## Visión del Proyecto
Este análisis busca responder preguntas como:
- ¿Qué tan frecuentemente las ciudades estudiadas superan los niveles recomendados por la OMS?
- ¿Existen patrones temporales que muestren días o periodos críticos?
- ¿Qué ciudad presenta mayor exposición a altos niveles de PM2.5 en los últimos 90 días?

## Ciudades Analizadas
Se han seleccionado las siguientes ciudades representativas de distintas regiones iberoamericanas:
- **Santiago** (Chile)
- **Ciudad de México** (México)
- **Río de Janeiro** (Brasil)
- **Madrid** (España)

## Resultados Principales

### 1. Porcentaje de días sobre el límite OMS (últimos 90 días)
![Porcentaje de días sobre OMS](barras_pct_sobre_oms.png)

- **Santiago**: 95.5% de los días por encima del límite OMS.
- **Ciudad de México**: 68.1%.
- **Río de Janeiro**: 30.4%.
- **Madrid**: 26.4%.

**Interpretación:** Santiago presenta una situación crítica, con casi todos los días del periodo por encima del valor recomendado, seguida por Ciudad de México. En contraste, Madrid y Río de Janeiro muestran niveles relativamente más bajos, aunque aún con una proporción significativa de días en alerta.

### 2. Evolución diaria de PM2.5
![Evolución diaria PM2.5](lineas_pm25.png)

- **Santiago** exhibe picos muy altos y recurrentes, alcanzando concentraciones superiores a 80 µg/m³.
- **Ciudad de México** muestra variabilidad moderada, con múltiples días sobre el umbral.
- **Madrid** y **Río de Janeiro** se mantienen mayormente por debajo del límite, aunque con algunos eventos puntuales de superación.

## Conclusiones
1. **Santiago** se posiciona como la ciudad con mayor riesgo de exposición a PM2.5 en este análisis, seguida por **Ciudad de México**.
2. Los datos evidencian que incluso ciudades con menor frecuencia de superación (Madrid y Río de Janeiro) no están exentas de episodios críticos.
3. Es fundamental promover medidas de control de emisiones, monitoreo constante y campañas de concientización ciudadana para reducir la exposición a este contaminante.
4. Este tipo de análisis puede servir como base para políticas públicas y estrategias de mitigación a nivel local y regional.

---
**Autor:** Yocce González  
**Repositorio:** [GitHub Pages](https://yoccegr.github.io)
