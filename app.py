import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. CONFIGURACIÓN INICIAL
# ==========================================
st.set_page_config(
    page_title="Video Games Analytics | Portafolio",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CARGA DE DATOS (Caché)
# ==========================================
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/video_games_sales.csv')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year', 'Global_Sales'])
    df['Year'] = df['Year'].astype(int)
    return df

df = load_data()

# ==========================================
# 3. PÁGINAS (MÓDULOS)
# ==========================================

def page_inicio():
    """Página 1: Índice y KPIs"""
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1: st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=70)
    with col2:
        st.title("Análisis Global del Mercado de Videojuegos")
        st.markdown("Bienvenido a esta aplicación web interactiva. Utiliza el menú lateral para navegar por las distintas perspectivas de análisis financiero y comercial del histórico de ventas de videojuegos (1980-2020).")
    with col3: st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=80)
    
    st.divider()
    
    st.subheader("Indicadores Clave de Rendimiento (KPIs)")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Volumen Total Ventas", f"{df['Global_Sales'].sum():,.0f} M")
    kpi2.metric("Títulos Lanzados", f"{len(df):,}")
    kpi3.metric("Plataformas Activas", f"{df['Platform'].nunique()}")
    kpi4.metric("Publishers Competidores", f"{df['Publisher'].nunique()}")
    
    st.info("👈 Selecciona una perspectiva en el menú lateral para comenzar el análisis.")

def page_temporal():
    """Página 2: Series de Tiempo"""
    st.title("📈 Dinámica Temporal de Ventas")
    st.markdown("Análisis longitudinal del crecimiento de la industria y el ciclo de vida de las consolas.")
    
    ventas_anuales = df.groupby('Year')['Global_Sales'].sum().reset_index()
    fig_area = px.area(ventas_anuales, x='Year', y='Global_Sales', 
                       title='Evolución Histórica de Ventas Globales',
                       color_discrete_sequence=['#2ecc71'])
    st.plotly_chart(fig_area, use_container_width=True)
    
    st.markdown("### Top Plataformas a lo largo del tiempo")
    top_platforms = df['Platform'].value_counts().head(5).index
    df_top_plat = df[df['Platform'].isin(top_platforms)]
    ventas_plat_anio = df_top_plat.groupby(['Year', 'Platform'])['Global_Sales'].sum().reset_index()
    
    fig_line = px.line(ventas_plat_anio, x='Year', y='Global_Sales', color='Platform',
                       title='Ciclo de Vida de las Consolas Líderes')
    st.plotly_chart(fig_line, use_container_width=True)

def page_regional():
    """Página 3: Comparativa Geográfica"""
    st.title("🌍 Perspectiva Regional")
    st.markdown("Comparativa de la penetración de mercado entre Norteamérica, Europa y Japón.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        regiones = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
        valores = [df[r].sum() for r in regiones]
        fig_pie = px.pie(names=['Norteamérica', 'Europa', 'Japón', 'Otros'], values=valores, 
                         hole=0.4, title='Cuota de Mercado Global por Región')
        fig_pie.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        genero_region = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()
        fig_bar = px.bar(genero_region, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales'], 
                         title='Preferencias de Género por Región', barmode='group')
        st.plotly_chart(fig_bar, use_container_width=True)

def page_publishers():
    """Página 4: Cuota de Mercado Corporativa"""
    st.title("🏢 Análisis Competitivo (Publishers)")
    
    top_n = st.slider("Selecciona el Top N de Publishers a analizar:", 5, 20, 10)
    top_pubs = df.groupby('Publisher')['Global_Sales'].sum().nlargest(top_n).reset_index()
    
    fig_tree = px.treemap(top_pubs, path=['Publisher'], values='Global_Sales',
                          color='Global_Sales', color_continuous_scale='Blues',
                          title=f'Jerarquía de Mercado: Top {top_n} Publishers')
    st.plotly_chart(fig_tree, use_container_width=True)
    
    st.markdown("### Rendimiento del Top 5 Publishers a lo largo del tiempo")
    top5 = top_pubs['Publisher'].head(5)
    df_top5 = df[df['Publisher'].isin(top5)].groupby(['Year', 'Publisher'])['Global_Sales'].sum().reset_index()
    fig_pub_line = px.line(df_top5, x='Year', y='Global_Sales', color='Publisher')
    st.plotly_chart(fig_pub_line, use_container_width=True)

def page_riesgo():
    """Página 5: Volatilidad y Riesgo (Enfoque Actuarial)"""
    st.title("⚖️ Riesgo y Volatilidad por Género")
    st.markdown("Esta perspectiva evalúa la dispersión estadística de las ventas. Una alta desviación estándar implica mayor riesgo financiero para los desarrolladores.")
    
    # Boxplot para ver outliers y dispersión
    fig_box = px.box(df, x='Genre', y='Global_Sales', color='Genre',
                     title='Dispersión de Ventas por Género (Identificación de Outliers)')
    # Limitamos el eje Y para que los mega-éxitos (como Wii Sports) no aplasten el gráfico
    fig_box.update_yaxes(range=[0, df['Global_Sales'].quantile(0.95)]) 
    st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("### Tabla de Resumen Estadístico")
    
    # 1. Agrupamos y calculamos
    resumen = df.groupby('Genre')['Global_Sales'].agg(['count', 'mean', 'std', 'max']).reset_index()
    
    # 2. Llenamos posibles valores nulos (NaN) con 0 para evitar errores visuales
    resumen = resumen.fillna(0)
    
    # 3. Renombramos las columnas
    resumen.columns = ['Género', 'Cantidad de Juegos', 'Media de Ventas (M)', 'Volatilidad (Std)', 'Venta Máxima']
    
    # 4. Renderizamos la tabla estilizada
    st.dataframe(
        resumen.style.background_gradient(cmap='Oranges', subset=['Volatilidad (Std)']), 
        use_container_width=True
    )


def page_datos():
    """Página 6: Explorador y Descarga"""
    st.title("🗄️ Explorador de Datos Crudos")
    st.markdown("Filtra la base de datos y descarga los resultados para auditoría.")
    
    genero = st.selectbox("Filtrar por Género:", ["Todos"] + list(df['Genre'].unique()))
    if genero != "Todos":
        df_show = df[df['Genre'] == genero]
    else:
        df_show = df
        
    st.dataframe(df_show, use_container_width=True)
    
    # Botón de descarga CSV nativo de Streamlit
    csv = df_show.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Datos Filtrados (CSV)",
        data=csv,
        file_name='video_games_filtrado.csv',
        mime='text/csv',
    )

# ==========================================
# 4. ENRUTADOR (Navegación en el Sidebar)
# ==========================================
def main():
    st.sidebar.title("Navegación")
    st.sidebar.markdown("Selecciona una perspectiva:")
    
    # Diccionario que mapea los nombres del menú a las funciones
    pages = {
        "🏠 Índice": page_inicio,
        "📈 Dinámica Temporal": page_temporal,
        "🌍 Perspectiva Regional": page_regional,
        "🏢 Análisis Competitivo": page_publishers,
        "⚖️ Riesgo y Volatilidad": page_riesgo,
        "🗄️ Explorador de Datos": page_datos
    }
    
    # Creamos el menú de radio buttons
    seleccion = st.sidebar.radio("Ir a:", list(pages.keys()))
    
    st.sidebar.divider()
    st.sidebar.caption("Desarrollado con ❤️ usando Python y Streamlit.")
    
    # Ejecutamos la función correspondiente a la página seleccionada
    pages[seleccion]()

if __name__ == "__main__":
    main()
