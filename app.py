import streamlit as st

# Define your QA function here
def qa_function(question):
    # Aquí va la lógica de tu función de QA
    # Por ahora, devolveremos una respuesta de ejemplo
    return "Esta es una respuesta de ejemplo a la pregunta: " + question

# Configuración de la interfaz de usuario en Streamlit
st.title("Plataforma de Preguntas y Respuestas")
st.write("Ingresa tu pregunta en el cuadro de texto a continuación y obtén una respuesta:")

# Entrada del usuario
user_question = st.text_input("Pregunta:")

# Al presionar el botón, se procesa la pregunta
if st.button("Enviar"):
    if user_question:
        # Llamada a la función de QA
        answer = qa_function(user_question)
        # Mostrar la respuesta
        st.write("Respuesta:", answer)
    else:
        st.write("Por favor, ingresa una pregunta.")

