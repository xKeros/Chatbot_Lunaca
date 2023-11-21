# Importar el backend
import b_backend
import streamlit as st
from streamlit_chat import message

# Configuración de Streamlit
st.title("CBOL 🤖")
st.write("Puedes hacerme las preguntas que necesites sobre errores de equipos de frío")

# Inicializar listas en el estado de la sesión para preguntas y respuestas
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

# Definir la función para manejar el clic en el botón Enviar
def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ''

# Crear el formulario de Streamlit
with st.form('my-form'):
    query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
    submit_button = st.form_submit_button('Enviar', on_click=click)

# Visualizar preguntas y respuestas
if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas)-1, -1, -1):
        st.text(f'Pregunta: {st.session_state.preguntas[i]}')
        st.text(f'Respuesta: {st.session_state.respuestas[i]}')

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []
