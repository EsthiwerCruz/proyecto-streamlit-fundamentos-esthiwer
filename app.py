import streamlit as st
##st.title("Mi primera aplicación en python")
st.sidebar.title("Segmentación")

##st.sidebar.selectbox('Home','Ejercicio 1')


opcion = st.sidebar.selectbox(
    'Menú',
    ['Home', 'Ejercicio 1', 'Ejercicio 2', 'Ejercicio 3','Ejercicio 4']
)
##st.write("Seleccionaste:", opcion)

#Contenido según selección:

if opcion == 'Home':

    st.title("📊 Proyecto Aplicado en Streamlit – Fundamentos de Programación")
    col4,col5 = st.columns(2)
    col1, col2 = st.columns(2)
    col3, = st.columns(1) 
    col6, = st.columns(1)
    
    with col4:
        st.image("C:\\Users\\usuario\\Pictures\\Dmc.png",width=200 )
    with col5:
        st.image("C:\\Users\\usuario\\Pictures\\Python.png",width=80 )


    with col1:
        st.info("""
        **Nombre:** Esthiwer Ken Cruz Ayte  
        **Curso:** Especialización en Python for Analytics  
        **Año:** 2026
        """)

    with col2:
        st.success("🚀 Módulo 1 - Proyecto Aplicado")

    with col3:

        st.markdown("---")

        st.markdown("""
        <u><b>Objetivo del trabajo:</b></u>

        Desarrollar una aplicación interactiva en Streamlit que integre los conceptos
        fundamentales aprendidos durante el Módulo 1 del curso.

        <u><b>Tecnologías utilizadas:</b></u>

        - Variables
        - Estructuras de datos
        - Control de flujo
        - Funciones
        - Programación funcional
        - Programación Orientada a Objetos (POO)

        Este proyecto servirá como base para la construcción de un portafolio personal.
        """, unsafe_allow_html=True) 

        st.markdown("---") 

    with col6:
        st.info("""
        **Puesto:** Analista de Gestión de Reclamos y solicitudes  
        **Empresa:** Seguros Falabella  
        """)
##-============================================================

if opcion == "Ejercicio 1":

    # Título del módulo
    st.title("💰 Verificador de Presupuesto")
    st.markdown("---")
    # Solicitar presupuesto
    presupuesto = st.number_input(
        "Ingrese el presupuesto:",
        min_value=0.0,
        format="%.2f"
    )
    # Solicitar gasto
    gasto = st.number_input(
        "Ingrese el gasto:",
        min_value=0.0,
        format="%.2f"
    )
    #  Botón para evaluar
    if st.button("Evaluar presupuesto"):

        diferencia = presupuesto - gasto

        # Evaluación
        if gasto <= presupuesto:
            st.success("✅ El gasto está dentro del presupuesto")
        else:
            st.warning("⚠️ El presupuesto fue excedido")

        # Mostrar diferencia
        st.write(f"Diferencia presupuesto - gasto: {diferencia:.2f}")

##-============================================================

if opcion == "Ejercicio 2":

    st.title("✅ Registro de actividades financieras")
    st.markdown("---")

    # 1️⃣ Crear lista si no existe
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    # 2️⃣ Inputs
    actividad = st.text_input("Nombre de la actividad")

    tipo = st.selectbox(
        "Tipo de actividad",
        ["Operativa", "Marketing", "Administrativa", "Inversión"]
    )

    presupuesto = st.number_input(
        "Ingrese el presupuesto:",
        min_value=0.0,
        format="%.2f"
    )

    gasto_real = st.number_input(
        "Ingrese el gasto real:",
        min_value=0.0,
        format="%.2f"
    )

    # 3️⃣ Botón agregar
    if st.button("Agregar actividad"):

        nueva_actividad = {
            "Actividad": actividad,
            "Tipo": tipo,
            "Presupuesto": presupuesto,
            "Gasto": gasto_real
        }

        st.session_state.actividades.append(nueva_actividad)

        st.success("Actividad agregada correctamente ✅")

    st.markdown("---")

    # 4️⃣ Mostrar tabla
    if st.session_state.actividades:

        st.subheader("📋 Lista de actividades")

        st.dataframe(st.session_state.actividades)

        st.markdown("---")

        # 5️⃣ y 6️⃣ Recorrer lista y evaluar
        st.subheader("📊 Evaluación de actividades")

        for act in st.session_state.actividades:

            if act["Gasto"] <= act["Presupuesto"]:
                estado = "✅ Dentro del presupuesto"
            else:
                estado = "⚠️ Presupuesto excedido"

            # 7️⃣ Mostrar estado
            st.write(
                f"Actividad: **{act['Actividad']}** | "
                f"Tipo: {act['Tipo']} | "
                f"Estado: {estado}"
            )
##===================================================

if opcion == "Ejercicio 3":

    st.title("📈 Cálculo de Retorno Esperado")
    st.markdown("---")

    # 1️⃣ Validar que existan actividades
    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("Primero debes registrar actividades en el Ejercicio 2")
    else:

        # 2️⃣ Inputs
        tasa = st.number_input(
            "Ingrese la tasa (%)",
            min_value=0.0,
            value=10.0
        ) / 100   # convertir a decimal

        meses = st.number_input(
            "Ingrese cantidad de meses",
            min_value=1,
            step=1
        )

        # 3️⃣ Definir función
        def calcular_retorno(actividad, tasa, meses):
            retorno = actividad["Presupuesto"] * tasa * meses
            return {
                "Actividad": actividad["Actividad"],
                "Retorno esperado": round(retorno, 2)
            }

        # 4️⃣ Botón ejecutar
        if st.button("Calcular retorno esperado"):

            resultados = list(
                map(
                    lambda act: calcular_retorno(act, tasa, meses),
                    st.session_state.actividades
                )
            )

            # 5️⃣ Mostrar resultados
            st.subheader("📊 Retorno por actividad")

            for r in resultados:
                st.write(
                    f"Actividad: **{r['Actividad']}** → "
                    f"Retorno esperado: S/ {r['Retorno esperado']}"
                )
##====================================================

if opcion == "Ejercicio 4":

    st.title("🏦 Gestión de Actividades - Programación Orientada a Objetos")

    # 1️⃣ Definir clase
    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        # 2️⃣ Método evaluación
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        # 3️⃣ Método resumen
        def mostrar_info(self):
            return (
                f"Actividad: {self.nombre} | "
                f"Tipo: {self.tipo} | "
                f"Presupuesto: S/ {self.presupuesto:.2f} | "
                f"Gasto: S/ {self.gasto_real:.2f}"
            )

    st.markdown("---")

    # 4️⃣ Verificar actividades del ejercicio 2
    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("⚠️ Primero registra actividades en el Ejercicio 2")
    else:

        st.subheader("📋 Evaluación usando Objetos")

        # Convertir diccionarios en objetos
        objetos_actividad = [
            Actividad(
                act["Actividad"],
                act["Tipo"],
                act["Presupuesto"],
                act["Gasto"]
            )
            for act in st.session_state.actividades
        ]

        # 5️⃣ Mostrar información
        for obj in objetos_actividad:

            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("✅ Dentro del presupuesto")
            else:
                st.warning("⚠️ Presupuesto excedido")

            st.markdown("---")

            


    



