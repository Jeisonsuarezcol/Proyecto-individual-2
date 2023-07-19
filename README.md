# Proyecto de Análisis de Datos de Telecomunicaciones

Este proyecto tiene como objetivo analizar los datos de telecomunicaciones de Argentina, obtenidos de la API de la web del Ente Nacional de Comunicaciones (ENACOM), y encontrar oportunidades de crecimiento para la compañía.

## Contexto

Las telecomunicaciones son la ciencia y la práctica de la transmisión de información a través de medios electromagnéticos, mediante el empleo de un conjunto de técnicas y materiales especializados. Dicha información puede consistir en datos textuales, de audio, de video o la combinación de los tres.

En Argentina, las telecomunicaciones se brindan en forma telegráfica, telefónica, postal, emisión de canales de televisión, radios y provisión de conexión a internet abarcando todo el territorio nacional. El país está a la vanguardia en el desarrollo de las telecomunicaciones y ha experimentado un incremento del 200% en el acceso a Internet de fibra óptica en toda la Argentina. 

## Objetivos

- Realizar un análisis para reconocer el comportamiento del sector de telecomunicaciones en Argentina.
- Orientar a la empresa en brindar una buena calidad de sus servicios.
- Identificar oportunidades de crecimiento.

## Fuentes de datos

Los datos utilizados para este proyecto provienen de la API de ENACOM, que ofrece información sobre los servicios y operadores de telecomunicaciones en Argentina. La API se puede consultar desde este link: [API](https://datosabiertos.enacom.gob.ar/developers/). 
Los datos se descargaron en formato csv y se almacenaron en la carpeta Datasets del repositorio.

## Contenido

El repositorio contiene los siguientes archivos y carpetas:

- `EDA PI N°2`: un notebook de Jupyter donde se realiza el análisis exploratorio de datos (EDA) con pasos documentados, cargando los datos desde la API de ENACOM y usando gráficos de barras, líneas, dispersión y barras agrupadas para visualizar las tendencias y patrones de los datos.
- `Dashboard PI 2`: un archivo de Power BI donde se crea un dashboard interactivo que incluye indicadores clave de rendimiento (KPI) como el porcentaje de ingresos anuales de los operadores por tipo de tecnología (ADSL, Cablemodem, Fibra óptica, Wireless), el ingreso promedio por usuario (ARPU), el porcentaje de ingresos anuales promedio de los operadores y un mapa que muestra los servicios de telecomunicaciones disponibles en cada región del país.
- `Introducción.py`: un archivo de Python donde se crea una visualización con Streamlit que muestra las gráficas del EDA y permite interactuar con algunas de ellas. El acceso a esta visualización se puede hacer desde este link: [].
- `Datasets`: una carpeta que contiene los archivos csv con los datos utilizados para el archivo de Power BI y la visualización de Streamlit.

## Requisitos

Para ejecutar el notebook se requieren las siguientes librerías de Python:

- pandas
- numpy
- matplotlib
- seaborn
- requests