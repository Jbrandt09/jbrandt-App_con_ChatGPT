import streamlit as st

# Configuración del título y del autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por Jornell Brandt.")

# Pregunta al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Imprime un mensaje de bienvenida utilizando el nombre proporcionado por el usuario
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
