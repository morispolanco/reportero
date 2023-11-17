import streamlit as st
import requests

def main():
    st.title("Reportero")

    # Configurar la URL base y los encabezados
    url = 'https://api.respell.ai/v1/run'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805',
        'Content-Type': 'application/json'
    }

    # Entrada de texto del usuario
    input_text = st.text_input("Ingrese los datos de la noticia", "accidente, ruta al Pacífico, tres fallecidos...")

    if st.button("Enviar"):
        # Crear el cuerpo de la solicitud
        data = {
            "spellId": "YiTnWQ0VLkGdU16i7bYLy",
            "spellVersionId": "b24eBWzc5rNXzISlb4LjK",
            "inputs": {
                "input": input_text
            }
        }

        # Realizar la solicitud POST a la API
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            st.success("Respuesta exitosa:")
            st.json(response.json())
        else:
            st.error("Error en la solicitud. Código de estado: " + str(response.status_code))

if __name__ == "__main__":
    main()
