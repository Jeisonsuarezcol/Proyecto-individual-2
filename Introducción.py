import streamlit as st

def main():
    st.title("Proyecto de Análisis de Datos de Telecomunicaciones")

    st.markdown(
        """
        Este proyecto tiene como objetivo analizar los datos de telecomunicaciones de Argentina, 
        obtenidos de la API de la web del Ente Nacional de Comunicaciones (ENACOM), y encontrar 
        oportunidades de crecimiento para la compañía.
        """
    )

    st.markdown("## Contexto")

    st.markdown(
        """
        Las telecomunicaciones son la ciencia y la práctica de la transmisión de información a través de medios 
        electromagnéticos, mediante el empleo de un conjunto de técnicas y materiales especializados. Dicha información 
        puede consistir en datos textuales, de audio, de video o la combinación de los tres.

        En Argentina, las telecomunicaciones se brindan en forma telegráfica, telefónica, postal, emisión de canales de 
        televisión, radios y provisión de conexión a internet abarcando todo el territorio nacional. El país está a la 
        vanguardia en el desarrollo de las telecomunicaciones y ha experimentado un incremento del 200% en el acceso a 
        Internet de fibra óptica en toda la Argentina. El gobierno impulsa constantemente la mejora de las TIC para que 
        todos los argentinos puedan acceder a servicios de telefonía fija y móvil, de internet, de comunicación audiovisual 
        y postales con la máxima calidad, diversidad, competencia y pluralidad.
        """
    )

    st.markdown("## Objetivos")

    st.markdown(
        """
        - Realizar un análisis para reconocer el comportamiento del sector de telecomunicaciones en Argentina.
        - Orientar a la empresa en brindar una buena calidad de sus servicios.
        - Identificar oportunidades de crecimiento.
        """
    )

    st.markdown("## Fuentes de datos")

    st.markdown(
        """
        Los datos utilizados para este proyecto provienen de la API de ENACOM, que ofrece información sobre los servicios 
        y operadores de telecomunicaciones en Argentina. La API se puede consultar desde este link: 
        [API](https://datosabiertos.enacom.gob.ar/developers/).

        Los datos se descargaron en formato csv y se almacenaron en la carpeta Datasets del repositorio.
        """
    )


if __name__ == "__main__":
    main()
