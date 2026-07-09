import streamlit as st
st.title("Aplicación de Fundamentos Streamlit")
st.sidebar.image("REDYCOMPU - imagen portada facebook.png")
st.sidebar.title("Parámetros")
monto = st.number_input("Ingrese el monto de su prestamo", value = 5000)

interes = st.number_input("Ingrese el interes", value = 0.05)

tiempo_meses = st.number_input("Ingrese el tiempo en meses", value = 12)

resultado = monto*interes*(tiempo_meses/12)
st.write("El resultado es: ", resultado)
