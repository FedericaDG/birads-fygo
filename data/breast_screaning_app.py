
import streamlit as st

# Configuración general de la página
st.set_page_config(page_title="Asistente de Estudios Mamarios", layout="centered")

# Encabezado
st.title("Asistente para estudios mamarios")
st.markdown("---")

# Entrada de edad
st.markdown("### Edad de la paciente")
edad = st.number_input("¿Cuántos años tenés?", min_value=15, max_value=100, step=1)

# Antecedentes familiares
st.markdown("### Antecedentes familiares de cáncer de mama")
riesgo = st.radio(
    "¿Tenés familiares directos con cáncer de mama? (madre, hermana, hija, abuela < 60 años)",
    ("Sí", "No")
)

# Prótesis mamarias
st.markdown("### Prótesis mamarias")
protesis = st.radio("¿Tenés prótesis mamarias?", ("Sí", "No"))

# Mostrar estudios sugeridos según edad, riesgo y prótesis
if edad:
    estudios = []
    if edad < 35:
        estudios.append("Ecografía mamaria")
        if protesis == "Sí":
            estudios.append("Resonancia magnética")
    elif 35 <= edad < 40:
        estudios.append("Ecografía mamaria")
        if riesgo == "Sí":
            estudios.append("Mamografía")
    elif edad >= 40:
        estudios.extend(["Mamografía", "Ecografía mamaria"])
    if riesgo == "Sí" and edad >= 30:
        estudios.append("Mamografía anual desde los 30 años")

    st.markdown("### Estudios sugeridos:")
    for e in estudios:
        st.write(f"• {e}")

# Ingreso de BI-RADS
st.markdown("---")
st.markdown("### Resultados de estudios (opcional)")
birads_eco = st.selectbox("BIRADS de la ecografía", ["", "1", "2", "3", "4", "5", "6", "0"])
birads_mx = st.selectbox("BIRADS de la mamografía", ["", "1", "2", "3", "4", "5", "6", "0"])
birads_rm = st.selectbox("BIRADS de la resonancia magnética", ["", "1", "2", "3", "4", "5", "6", "0"])

# Determinar la prioridad
prioridad = None
for val in ["6", "5", "4", "3", "2", "1", "0"]:
    if val in [birads_eco, birads_mx, birads_rm]:
        prioridad = val
        break

# Recomendación final según BI-RADS
if prioridad:
    st.markdown("---")
    st.markdown("### Recomendación final")
    if prioridad == "0":
        st.warning("Estudio no concluyente. Se sugieren estudios complementarios.")
    elif prioridad == "3":
        st.info("BIRADS 3: Seguí con control a los 6 meses.")
    elif prioridad in ["4", "5", "6"]:
        st.error(f"BIRADS {prioridad}: Consultá con tu médica para seguimiento especializado.")
    elif prioridad in ["1", "2"]:
        st.success(f"BIRADS {prioridad}: Seguimiento habitual según indicación médica.")

# Autoexamen
st.markdown("---")
st.info("🧠 No te olvides del autoexamen mamario mensual.")
if st.button("¿Cómo se hace el autoexamen?"):
    st.video("https://www.youtube.com/watch?v=y48E3LwswMk")

