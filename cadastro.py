import streamlit as st
import pandas as pd
from datetime import date

def garvar_dados(nome, data_nasc, tipo):
    # Verifica se todos os campos estão preenchidos corretamente
    if nome and data_nasc:
        # Calcula a idade
        idade = (date.today() - data_nasc).days // 365  # Aproximação da idade em anos
        
        # Verifica se a idade está entre 0 e 150 anos
        if 0 <= idade <= 150:
            # Formata a data de nascimento para o formato DD/MM/AAAA
            data_nasc_formatada = data_nasc.strftime("%d/%m/%Y")
            with open("clientes.csv", "a", encoding="utf-8") as file:
                file.write(f"{nome},{data_nasc_formatada},{tipo}\n")  # Grava os dados formatados
            st.session_state["sucesso"] = True
        else:
            st.session_state["sucesso"] = False
            st.session_state["erro_idade"] = "A idade deve estar entre 0 e 150 anos."
    else:
        st.session_state["sucesso"] = False

# Configuração da página
st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="🐬"
)

st.title("Cadastro de clientes")
st.divider()

# Inputs do usuário
nome = st.text_input("Digite o nome do cliente", key="nome_cliente")
data_nasc = st.date_input("Data nascimento", format="DD/MM/YYYY") 
tipo = st.selectbox("Tipo do cliente", ["Pessoa jurídica", "Pessoa física"])

# Botão para cadastrar
btn_cadastrar = st.button("Cadastrar", on_click=garvar_dados, args=[nome, data_nasc, tipo])

# Mensagem de feedback ao usuário
if 'sucesso' in st.session_state:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Houve algum problema no cadastro!", icon="❌")
        
        # Mensagem específica sobre a idade
        if 'erro_idade' in st.session_state:
            st.error(st.session_state["erro_idade"], icon="⚠️")