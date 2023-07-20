import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import requests
import json

df_acc_hogares = pd.read_csv('Datasets/Acc_hogares.csv')
df_banda = pd.read_csv('Datasets/Tipo_banda.csv')
df_acc_tecnologia = pd.read_csv('Datasets/Acc_tecnologia.csv')

df_acc_tecnologia_prov = pd.read_csv('Datasets/Acc_tecnologia_prov.csv')
df_acc_tecnologia_prov['fecha'] = pd.to_datetime(df_acc_tecnologia_prov['fecha'])

df_velocidad_media = pd.read_csv('Datasets/Velocidad_media.csv')
df_velocidad_media['fecha'] = pd.to_datetime(df_velocidad_media['fecha'])


st.markdown('##### El siguiente Gráfico muestra las 5 provincias que han tenido mejores números de accesibilidad a lo largo del tiempo')

# Fitro de las 4 provincias con mejores números de accesibilidad
provincias_top4 = df_acc_hogares.groupby('Provincia')['Accesos por cada 100 hogares'].mean().nlargest(5).index

#provincias_top4 = provincias_top4[1:]
df_top4 = df_acc_hogares[df_acc_hogares['Provincia'].isin(provincias_top4)]

# Creamos una columna "Fecha" basada en el trimestre
df_top4['Fecha'] = df_top4.apply(lambda row: pd.to_datetime(str(row['Año']) + 'Q' + str(row['Trimestre'])), axis=1)

#Gráfico de líneas para cada provincia
fig, ax = plt.subplots(figsize=(12, 8))

for provincia in provincias_top4:
    df_provincia = df_top4[df_top4['Provincia'] == provincia]
    ax.plot(df_provincia['Fecha'], df_provincia['Accesos por cada 100 hogares'], label=provincia)

#Etiquetas
ax.set_xlabel('Fecha')
ax.set_ylabel('Accesos por cada 100 hogares')
ax.set_title('Provincias con mejores números de accesibilidad')
ax.legend()

st.pyplot(fig)


st.markdown('El gráfico anterior muestra las 5 provincias con un crecimiento sostenido en el tiempo respecto a accesos por cada 100 hogares, la provincia con más accesos históricamente ha sido la Capital Federal, su promedio para el tercer trimestre de 2022 supera los 120 accesos por cada 100 hogares, por la cantidad de habitantes de esta ciudad y a los servicios de telecomunicaciones de diversas organizaciones, haciendo que la media  sea superior a 100.')
st.markdown('La provincia Tierra Del Fuego presenta algo de variabilidad en sus cifras a lo largo del tiempo, esto puede deberse al tamaño de su población y otras causas externas. Las provincias de La Pampa, Córdoba y Buenos Aires presentan un crecimiento sostenido de sus cifras, por lo general el acceso por hogares en el país tiende a amentar cada año.')

st.markdown('***')



st.markdown('#### Provincias con mejores velocidades de bajada')

# Fitro de las 5 provincias con mejores velocidades
provincias_top5 = df_velocidad_media.groupby('Provincia')['Mbps (Media de bajada)'].max().nlargest(6).index
df_top5 = df_velocidad_media[df_velocidad_media['Provincia'].isin(provincias_top5)]

# Creamos una columna "Fecha" basada en el trimestre
df_top5['Fecha'] = df_top5.apply(lambda row: pd.to_datetime(str(row['Año']) + 'Q' + str(row['Trimestre'])), axis=1)

#Gráfico de líneas para cada provincia
fig, ax = plt.subplots(figsize=(12, 8))

for provincia in provincias_top5:
    df_provincia = df_top5[df_top5['Provincia'] == provincia]
    ax.plot(df_provincia['Fecha'], df_provincia['Mbps (Media de bajada)'], label=provincia)

#Etiquetas
ax.set_xlabel('Fecha')
ax.set_ylabel('Mbps (Media de bajada)')
ax.legend()

# Ajustes en el rango del eje x y el eje y
plt.xlim(df_provincia['Fecha'][507], 19300)

st.pyplot(fig)

st.markdown('En el anterior gráfico se muestran las 5 provincias con mayor media de bajada hasta la fecha, lo que concluye que históricamente la capital ha tenido las mejores velocidades y que las velocidades en el resto de las provincias aumentan con los años, esto indica que las personas tienden a contratar mejores planes, dándonos una visión de cómo mejorar los servicios prestados, aumentando la tasa de retención de clientes y con ello las ganancias.')

st.markdown('***')



st.markdown('#### Comparación entre Banda ancha fija y Dial up')

# Filtro de las 5 provincias por tipo de conexión. 

provincias_top5 = df_banda.groupby('Provincia')['Dial up'].max().nlargest(5).index
df_top5 = df_banda[df_banda['Provincia'].isin(provincias_top5)]
banda_ancha = df_top5['Banda ancha fija'].tail(5)
dial_up = df_banda.groupby('Provincia')['Dial up'].max().nlargest(5).values
provincia = provincias_top5.to_list()

# Crear un array de posiciones para las barras
x = np.arange(len(provincia))

# Ancho de las barras
bar_width = 0.35

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar las barras para Banda ancha fija
rects1 = ax.bar(x, banda_ancha, bar_width, color='blue', label='Banda ancha fija')

# Graficar las barras para Dial up
rects2 = ax.bar(x + bar_width, dial_up, bar_width, color='red', label='Dial up')

# Agregamos etiquetas en el eje x
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(provincia, rotation=45)

# Etiquetas de los ejes
ax.set_xlabel('Provincia')
ax.set_ylabel('Valores en Millones')
ax.legend()

st.pyplot(fig)

st.markdown('En el anterior gráfico se muestra la comparación entre banda ancha fija y Dial up, se hace evidente que la mayoría de las conexiones se hacen por banda ancha fija y que Dial up aporta poco más del 1% del total, esto es debido a que la velocidad de conexión con dial-up es muy lenta en comparación con otras formas de conexión a internet.')

st.markdown('***')



st.markdown('#### Número de accesos por tipo de tecnología')

categorias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']

agrupado =df_acc_tecnologia.groupby('Año').sum()

anio = 8
valor = 2022

st.markdown('Seleccionar Año:')

a,b,c,d,e,f,g,h,j =  st.columns(9)
ind =0
for  i in a,b,c,d,e,f,g,h,j:
    with i:
        if st.button(f'{agrupado.index[ind]}'):
            anio = ind
            valor = agrupado.index[ind]
    ind +=1

valores = agrupado.iloc[anio,1:6].tolist()

# Creamos un nuevo DataFrame utilizando las listas de categorías y valores
data = pd.DataFrame({'Tipo de tecnología': categorias, 'Valores': valores})

# Dividimos los valores por un millón para mostrarlos en millones
data['Número de accesos (M)'] = data['Valores'] / 1000000

# Se genera el Catplot utilizando la columna de Valores (M)
plot = sns.catplot(x='Tipo de tecnología', y='Número de accesos (M)', data=data, kind='bar')

# Creamos un objeto de formateo para mostrar los valores en millones
formatter = ticker.FuncFormatter(lambda x, pos: f'{x}M')

# Aplicamos el formateo a los ticks del eje y
plot.ax.yaxis.set_major_formatter(formatter)

plot.set_xticklabels(categorias, rotation=15)

plt.title(f'Año {valor}')

st.pyplot(plot)


st.markdown('En el anterior gráfico se muestra el número de accesos por tipo de tecnología, este gráfico varía según el año en que se configure, mostrando que tecnologías como ADSL han disminuido sus accesos con el tiempo, y tecnologías como Cablemódem y Fibra óptica han aumentado. Con lo anterior se deben mejorar la calidad de los servicios si queremos aumentar la fidelización de clientes y ampliar el rango de personas que pueden acceder a este tipo de tecnologías mejorando la infraestructura disponible.')

st.markdown('***') 



st.markdown('#### Número de accesos por tipo de tecnología y provincia')

# Datos para los conjuntos de barras
x = df_acc_tecnologia_prov.groupby('Provincia')['Total'].mean().nlargest(5).index

df_top5 = df_acc_tecnologia_prov[df_acc_tecnologia_prov['Provincia'].isin(x)]

df_top5 = df_top5[['Provincia','Cablemodem','Fibra óptica','ADSL','Wireless','Otros']].head().sort_values(by=['Cablemodem'], ascending = False)

y1 = [i / 1000000 for i in df_top5['Cablemodem']]
y2 = [i / 1000000 for i in df_top5['Fibra óptica']]
y3 = [i / 1000000 for i in df_top5['ADSL']]
y4 = [i / 1000000 for i in df_top5['Wireless']]
y5 = [i / 1000000 for i in df_top5['Otros']]

# Creamos el gráfico de barras sobrepuesto
width = 0.55  # Ancho de las barras
offsets = np.linspace(-2 * width, 2 * width, 5)  # Desplazamientos

# Definimos el tamaño de la figura con figsize
fig1 = plt.figure(figsize=(8, 6))

plt.bar(x, y1, width=width, color='blue', alpha=0.6, label='Cablemodem', align='center', edgecolor='black')
plt.bar(x, y2, width=width, color='red', alpha=0.7, label='Fibra óptica', align='edge', edgecolor='black')
plt.bar(x, y3, width=width, color='yellow', alpha=0.7, label='ADSL', align='edge', edgecolor='black')
plt.bar(x, y4, width=width, color='green', alpha=0.7, label='Wireless', align='edge', edgecolor='black')
plt.bar(x, y5, width=width, color='purple', alpha=0.7, label='Otros', align='edge', edgecolor='black')

# Añadimos etiquetas y título al gráfico
plt.xlabel('Provincia')
plt.ylabel('Número de accesos (M)')

plt.xticks(rotation=15)

formatter = ticker.FuncFormatter(lambda x, pos: f'{round(x,1)}M')
plt.gca().yaxis.set_major_formatter(formatter)

plt.legend()

st.pyplot(fig1)

st.markdown('En el anterior gráfico se muestra cómo se distribuye la tecnología en cada provincia, con datos del tercer trimestre del 2022, nuevamente podemos decir que tecnologías como Cablemódem y Fibra óptica aumentaron su número de accesos, esta vez tenemos organizados los datos por las provincias con mayores accesos, lo que indica que son las provincias con mayor tasa de acceso por habitantes, ya que tienen la mayoría de la población del país.')



st.markdown('***') 

st.markdown('#### Relación entre accesos por cada 100 hogares y velocidad media de bajada')

fig, ax = plt.subplots()

plt.scatter(df_acc_hogares['Accesos por cada 100 hogares'], df_velocidad_media['Mbps (Media de bajada)'], alpha=0.5)

# Personalización el scatter plot
plt.xlabel("Accesos por cada 100 hogares")
plt.ylabel("Mbps (Media de bajada)")

st.pyplot(fig)

st.markdown('En el anterior gráfico de dispersión tenemos una cierta correlación positiva entre la velocidad media de bajada y los accesos por cada 100 hogares, esta información es importante porque indica que en las zonas donde hay mayor tasa de acceso al servicio las velocidades tienden a ser más altas.')



st.markdown('***') 

st.markdown('#### Relación entre tipo de tecnología y velocidad de bajada')

# Creación de los datos
df_trimestral = df_acc_tecnologia_prov.groupby(pd.Grouper(key='fecha', freq='Q')).sum()

df_velocidad_media = df_velocidad_media[['Año','Trimestre','Mbps (Media de bajada)','fecha']]
df_trimestral2 = df_velocidad_media.groupby(pd.Grouper(key='fecha', freq='Q')).mean()

año = df_trimestral.index
categoria1 = df_trimestral['Cablemodem']/1000000
categoria2 = df_trimestral['Fibra óptica']/1000000
categoria3 = df_trimestral2['Mbps (Media de bajada)']

# Figura y primer eje
fig, ax1 = plt.subplots()
ax1.plot(año, categoria1, color="blue", alpha=0.5, label="Cablemodem")
ax1.plot(año, categoria2, color="blue", label="Fibra óptica")
ax1.set_xlabel("Año")
ax1.set_ylabel("Suma de accesos por Tipo de tecnología", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

formatter = ticker.FuncFormatter(lambda x, pos: f'{round(x)}M')
plt.gca().yaxis.set_major_formatter(formatter)

# Creamos el segundo eje que comparte el mismo eje x
ax2 = ax1.twinx()
ax2.plot(año, categoria3, color="green")
ax2.set_ylabel("Mbps (Media de bajada)", color="green")
ax2.tick_params(axis="y", labelcolor="green")

# Agregamos leyendas al primer eje
ax1.legend()

# Mostrar gráfica
st.pyplot(fig)

st.markdown('Este gráfico cuenta con doble eje y en el cual se expresa la relación que exite entre las tecnologías de conexión con mayores accesos en la actualidad (izquierda) y la velocidad media de bajada medida en Mbsp (derecha), se hace evidente que el tipo de conexión influye bastante el las velocidades de bajada, es importante recalcar que en las últimas visualizaciones el número o tasa te accesos tiene una fuerte reación con la población total de esos lugares por lo cuál no siempre es lo más inteligente aumentar la covertura de los sericios en zonas con menos población sino mejorar la covertura existente.')
