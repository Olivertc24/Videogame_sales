# Introducción

La industria del entretenimiento interactivo ha experimentado una transformación radical en las últimas cuatro décadas, evolucionando de un nicho tecnológico a convertirse en uno de los sectores económicos más influyentes a nivel global, superando en ingresos a industrias tradicionales como el cine y la música. Sin embargo, detrás de las cifras macroeconómicas, el mercado de los videojuegos se caracteriza por una alta **volatilidad estocástica**: el éxito de un título no es un evento determinista, sino el resultado de una compleja interacción entre variables demográficas, tecnológicas y culturales.

Para el profesional en Ciencias Actuariales y Ciencia de Datos, este sector presenta un desafío fascinante: ¿Es posible modelar la incertidumbre de las ventas globales? ¿Existen patrones históricos estacionarios que permitan predecir el comportamiento de futuros lanzamientos?

El presente trabajo de investigación tiene como propósito realizar un análisis estadístico exhaustivo sobre el conjunto de datos \textit{"Video Game Sales"}, el cual abarca más de 16,500 registros de ventas desde 1980 hasta 2020. A través del uso de herramientas computacionales avanzadas en **R** y técnicas de visualización de datos, se busca descomponer la varianza de las ventas en función de factores críticos como el Género, la Plataforma y la Región Geográfica (Norteamérica, Europa y Japón).

## Estructura del Informe

Este documento técnico se encuentra estructurado en cinco capítulos fundamentales:

\begin{itemize}
    \item En el \textbf{Capítulo I}, se plantea la problemática de la imprevisibilidad financiera en el desarrollo de software de entretenimiento, formulando las preguntas de investigación y delimitando el alcance temporal y geográfico del estudio.
    
    \item El \textbf{Capítulo II} establece el Marco Teórico, definiendo los conceptos estadísticos clave como esperanza matemática, series de tiempo y correlación, necesarios para la interpretación de los datos.
    
    \item El \textbf{Capítulo III} describe el Marco Metodológico, detallando el proceso de limpieza de datos (ETL), las pruebas de hipótesis y los algoritmos utilizados para validar la calidad de la información.
    
    \item El \textbf{Capítulo IV} presenta el Análisis de Resultados, donde se exhiben las tablas y gráficos generados dinámicamente, discutiendo los hallazgos sobre la concentración de mercado (Ley de Pareto) y la dinámica temporal.
    
    \item Finalmente, en el \textbf{Capítulo V}, se exponen las Conclusiones y Recomendaciones estratégicas derivadas del análisis cuantitativo, orientadas a la toma de decisiones basada en datos (\textit{Data-Driven Decision Making}).
\end{itemize}

Este reporte no solo pretende ofrecer una radiografía del pasado de la industria, sino también establecer una metodología reproducible para el análisis de riesgo en portafolios de productos digitales.

# Planteamiento del Problema

La industria global de los videojuegos ha evolucionado desde un nicho de entretenimiento tecnológico hasta convertirse en uno de los sectores económicos más lucrativos y volátiles del mundo. Sin embargo, para los inversores y desarrolladores (Publishers), el lanzamiento de un nuevo título conlleva un **riesgo financiero significativo**. La variabilidad en las ventas es extrema: mientras unos pocos títulos alcanzan ventas multimillonarias ("Outliers"), la gran mayoría no logra recuperar los costos de desarrollo.

Desde una perspectiva actuarial y de ciencia de datos, el problema no radica solo en maximizar las ventas, sino en **modelar la incertidumbre** asociada a un lanzamiento. Factores como la plataforma, el género, y la región geográfica (Norteamérica, Europa, Japón) introducen variables de confusión que dificultan la predicción lineal del éxito comercial.

La ausencia de un modelo claro que cuantifique cómo estas variables categóricas impactan en la esperanza matemática de las ventas genera ineficiencias en la asignación de presupuestos y en la gestión de inventarios físicos y digitales.

Argumento final. Debido a esto, se plantea las siguientes preguntas de investigación:

**1.** ¿Existe una tendencia estocástica estacionaria en el volumen de ventas globales a lo largo de las últimas tres décadas, o estamos ante un cambio estructural del mercado?

**2.** ¿De qué manera las preferencias regionales (NA, EU, JP) condicionan la probabilidad de éxito de un videojuego según su género?

**3.** ¿Cuáles son los factores determinantes (Plataforma, Publisher, Género) que maximizan la esperanza de venta en el mercado actual?

## Justificación

La justificación de este trabajo de investigación reside en la necesidad de aplicar técnicas estadísticas rigurosas y herramientas de **Business Intelligence** para mitigar la incertidumbre financiera en el sector. 

Desde el punto de vista práctico, los resultados permitirán a los "stakeholders" tomar decisiones basadas en datos (Data-Driven Decisions) sobre en qué géneros invertir o en qué plataformas desarrollar. Desde el punto de vista académico, este estudio aporta una metodología replicable utilizando **R y LaTeX** para el análisis exploratorio y descriptivo de grandes volúmenes de datos transaccionales, sirviendo como material de referencia para estudiantes de estadística y computación.

## Objetivos 

### Objetivo General

Analizar los patrones históricos y los factores determinantes en las ventas globales de videojuegos (1980-2020) para caracterizar el comportamiento del mercado según regiones y categorías.


### Objetivos Específicos

\begin{enumerate}
  \item Describir la evolución temporal de las ventas globales, identificando tendencias, ciclos y puntos de inflexión en la serie de tiempo.
  \item Determinar la influencia de las variables categóricas (Género y Plataforma) en la distribución de las ventas por región geográfica (Norteamérica, Europa y Japón).
  \item Generar un reporte técnico reproducible en formato PDF que integre visualizaciones estadísticas y tablas resumen utilizando RMarkdown y LaTeX.
\end{enumerate}

![Static Badge](https://img.shields.io/badge/HTML-red) ![Static Badge](https://img.shields.io/badge/R-blue) ![Static Badge](https://img.shields.io/badge/Python-yellow) 
