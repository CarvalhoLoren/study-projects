import requests                                

import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response = requests.get(endpoint)
    letra = response.json()['lyrics'] if response.status_code == 200 else "" 
    return letra

st.image("https://images.pexels.com/photos/167587/pexels-photo-167587.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
st.title("Letras de musica")

banda = st.text_input("Digite o nome da Banda: ", key ='banda')

musica = st.text_input('Digite o nome da Música: ', key='musica')

pesquisar = st.button('Pesquisar', key='pesquisar')

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a sua letra!")
        st.text(letra)
    else:
        st.error("Infelizmente não foi possivel encontrar a sua letra")
