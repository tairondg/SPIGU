import streamlit as st
import pesquisas.triagem as triagem
import pesquisas.carr_inicial as carr_inicial
import pesquisas.desc_interna as desc_interna
import pesquisas.rec_final as rec_final
import pesquisas.exp_final as exp_final
import datetime

logo_um = "image\GU_logo_um.png"

# CONFIGURAÇÃO DA PAGINA
st.set_page_config(
     page_title="SPIGU - Cosmópolis",
     page_icon="🚚",
     layout="wide",
     initial_sidebar_state="expanded",
    )

# RETIRAR MENU STREAMLIT
hide_st_style = """
            <style>
            base='dark'
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.sidebar.image(logo_um)
st.sidebar.subheader("Sistema de Pesagens Interna")
st.sidebar.write("")
status = st.sidebar.radio('STATUS',('PRÉ-PESAGEM', 'CARREGAMENTO INTERNO', 'DESCARGA INTERNA', 'RECEBIMENTO FINAL', 'EXPEDIÇÃO FINAL'))


if status == 'PRÉ-PESAGEM':
    st.title("PRÉ-PESAGEM")
    triagem.triagem()

if status == 'CARREGAMENTO INTERNO':
    st.title("CARREGAMENTO INTERNO")
    carr_inicial.carregamento_inicial()

if status == 'DESCARGA INTERNA':
    st.title("DESCARGA INTERNA")
    desc_interna.descargainterna()

if status == 'RECEBIMENTO FINAL':
    st.title("RECEBIMENTO FINAL")
    rec_final.recebimento_final()

if status == 'EXPEDIÇÃO FINAL':
    st.title("EXPEDIÇÃO FINAL")
    exp_final.expedicao_final()