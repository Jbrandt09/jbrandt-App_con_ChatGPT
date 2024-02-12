import streamlit as st

# Funciones de conversión
def temperatura(cantidad, tipo_conversion):
    if tipo_conversion == "Celsius a Fahrenheit":
        return cantidad * 9/5 + 32
    elif tipo_conversion == "Fahrenheit a Celsius":
        return (cantidad - 32) * 5/9
    elif tipo_conversion == "Celsius a Kelvin":
        return cantidad + 273.15
    elif tipo_conversion == "Kelvin a Celsius":
        return cantidad - 273.15

def longitud(cantidad, tipo_conversion):
    if tipo_conversion == "Pies a metros":
        return cantidad * 0.3048
    elif tipo_conversion == "Metros a pies":
        return cantidad / 0.3048
    elif tipo_conversion == "Pulgadas a centímetros":
        return cantidad * 2.54
    elif tipo_conversion == "Centímetros a pulgadas":
        return cantidad / 2.54

def peso(cantidad, tipo_conversion):
    if tipo_conversion == "Libras a kilogramos":
        return cantidad * 0.453592
    elif tipo_conversion == "Kilogramos a libras":
        return cantidad / 0.453592
    elif tipo_conversion == "Onzas a gramos":
        return cantidad * 28.3495
    elif tipo_conversion == "Gramos a onzas":
        return cantidad / 28.3495

def volumen(cantidad, tipo_conversion):
    if tipo_conversion == "Galones a litros":
        return cantidad * 3.78541
    elif tipo_conversion == "Litros a galones":
        return cantidad / 3.78541
    elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
        return cantidad * 16.3871
    elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
        return cantidad / 16.3871

def tiempo(cantidad, tipo_conversion):
    if tipo_conversion == "Horas a minutos":
        return cantidad * 60
    elif tipo_conversion == "Minutos a segundos":
        return cantidad * 60
    elif tipo_conversion == "Días a horas":
        return cantidad * 24
    elif tipo_conversion == "Semanas a días":
        return cantidad * 7

def velocidad(cantidad, tipo_conversion):
    if tipo_conversion == "Millas por hora a kilómetros por hora":
        return cantidad * 1.60934
    elif tipo_conversion == "Kilómetros por hora a metros por segundo":
        return cantidad / 3.6
    elif tipo_conversion == "Nudos a millas por hora":
        return cantidad * 1.15078
    elif tipo_conversion == "Metros por segundo a pies por segundo":
        return cantidad * 3.28084

def area(cantidad, tipo_conversion):
    if tipo_conversion == "Metros cuadrados a pies cuadrados":
        return cantidad * 10.7639
    elif tipo_conversion == "Pies cuadrados a metros cuadrados":
        return cantidad / 10.7639
    elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
        return cantidad * 0.386102
    elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
        return cantidad / 0.386102

def energia(cantidad, tipo_conversion):
    if tipo_conversion == "Julios a calorías":
        return cantidad / 4.184
    elif tipo_conversion == "Calorías a kilojulios":
        return cantidad * 4.184 / 1000
    elif tipo_conversion == "Kilovatios-hora a megajulios":
        return cantidad * 3.6
    elif tipo_conversion == "Megajulios a kilovatios-hora":
        return cantidad / 3.6

def presion(cantidad, tipo_conversion):
    if tipo_conversion == "Pascales a atmósferas":
        return cantidad / 101325
    elif tipo_conversion == "Atmósferas a pascales":
        return cantidad * 101325
    elif tipo_conversion == "Barras a libras por pulgada cuadrada":
        return cantidad * 14.5038
    elif tipo_conversion == "Libras por pulgada cuadrada a bares":
        return cantidad / 14.5038

def datos(cantidad, tipo_conversion):
    if tipo_conversion == "Megabytes a gigabytes":
        return cantidad / 1024
    elif tipo_conversion == "Gigabytes a terabytes":
        return cantidad / 1024
    elif tipo_conversion == "Kilobytes a megabytes":
        return cantidad / 1024
    elif tipo_conversion == "Terabytes a petabytes":
        return cantidad / 1024

# Lista de categorías de conversión
categorias = ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de datos"]

# Mostrar categorías en un menú desplegable
categoria_elegida = st.sidebar.selectbox("Selecciona una categoría", categorias)

# Selección de la conversión dentro de la categoría elegida
if categoria_elegida == "Temperatura":
    conversion = st.selectbox("Selecciona una conversión", ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = temperatura(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Longitud":
    conversion = st.selectbox("Selecciona una conversión", ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = longitud(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Peso/Masa":
    conversion = st.selectbox("Selecciona una conversión", ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = peso(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Volumen":
    conversion = st.selectbox("Selecciona una conversión", ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = volumen(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Tiempo":
    conversion = st.selectbox("Selecciona una conversión", ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = tiempo(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Velocidad":
    conversion = st.selectbox("Selecciona una conversión", ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = velocidad(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Área":
    conversion = st.selectbox("Selecciona una conversión", ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = area(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Energía":
    conversion = st.selectbox("Selecciona una conversión", ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = energia(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Presión":
    conversion = st.selectbox("Selecciona una conversión", ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = presion(cantidad, conversion)
    st.write(f"Resultado: {resultado}")

elif categoria_elegida == "Tamaño de datos":
    conversion = st.selectbox("Selecciona una conversión", ["Megabytes a gigabytes", "Gigabytes a terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"])
    cantidad = st.number_input("Ingresa la cantidad a convertir")
    resultado = datos(cantidad, conversion)
    st.write(f"Resultado: {resultado}")
