
import streamlit as st

# CONFIGURACIÓN
st.set_page_config(
    page_title="Calculadora de Varillas",
    page_icon="🏗️",
    layout="centered"
)

# DISEÑO
st.markdown("""
<style>
.stApp {
    background-color: #172B3A;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton button {
    background-color: #16A085;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 50px;
    border-radius: 10px;
}
.resultado {
    background-color: #145A32;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# TÍTULO
st.title("🏗️ CALCULADORA DE VARILLAS")
st.subheader("Selección de diámetro según el tramo de luz")

st.write(
    "Ingresa la longitud del tramo de la viga "
    "para obtener un diámetro de varilla recomendado."
)

st.markdown("---")

# ENTRADA
tramo = st.number_input(
    "📏 Longitud del tramo (metros):",
    min_value=0.01,
    max_value=100.0,
    value=3.0,
    step=0.10
)

# TABLA DE SELECCIÓN
st.subheader("📋 Tabla de selección")

st.table({
    "Longitud del tramo": [
        "Hasta 3 m",
        "Más de 3 hasta 4 m",
        "Más de 4 hasta 5 m",
        "Más de 5 m"
    ],
    "Diámetro de varilla": [
        "10 mm",
        "12 mm",
        "14 mm",
        "16 mm"
    ]
})

# CÁLCULO
if st.button("CALCULAR DIÁMETRO"):

    if tramo <= 3:
        diametro = 10

    elif tramo <= 4:
        diametro = 12

    elif tramo <= 5:
        diametro = 14

    else:
        diametro = 16

    st.markdown("---")

    st.markdown(
        f"""
        <div class="resultado">
            <h2>RESULTADO</h2>
            <h1 style="color:white;font-size:55px">
                Ø {diametro} mm
            </h1>
            <h3>Diámetro de varilla seleccionado</h3>
            <p>Longitud del tramo: {tramo:.2f} metros</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        f"Para un tramo de {tramo:.2f} m, "
        f"la regla de selección recomienda "
        f"una varilla de {diametro} mm."
    )

    st.info(
        "Esta selección es únicamente didáctica. "
        "El diámetro definitivo debe determinarse "
        "mediante el diseño estructural, considerando "
        "cargas, momentos, cortante, geometría y normativa."
    )
