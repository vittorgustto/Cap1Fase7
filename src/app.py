
import streamlit as st
from fase1_sensores import ler_sensores

st.set_page_config(page_title="Dashboard Integrada - FIAP", layout="wide")

st.title("Dashboard Integrada - Projeto FIAP")

fase = st.sidebar.selectbox("Selecione a Fase para Interagir", [
    "Fase 1 - Sensores",
    "Fase 2 - Banco de Dados",
    "Fase 3 - IoT",
    "Fase 6 - Visão Computacional"
])

if fase == "Fase 1 - Sensores":
    st.subheader("Monitoramento de Sensores")
    if st.button("Executar Leitura de Sensores"):
        temperatura, umidade = ler_sensores()
        st.markdown(f"**Sensor de Temperatura:** :blue[{temperatura}°C]")
        st.markdown(f"**Sensor de Umidade:** :green[{umidade}%]")

elif fase == "Fase 2 - Banco de Dados":
    st.subheader("Modelo Relacional de Dados")
    st.markdown("Código para criação do banco e inserção de dados disponível no arquivo `fase2_codigo.py`.")
    st.code(open("fase2_codigo.py").read(), language="python")

elif fase == "Fase 3 - IoT":
    st.subheader("Controle de Irrigação Inteligente")
    st.markdown("Simulação de sensores físicos e irrigação automática implementada no arquivo `fase3_iot.py`.")
    st.code(open("fase3_iot.py").read(), language="python")

elif fase == "Fase 6 - Visão Computacional":
    st.subheader("Análise com YOLOv5")
    if st.button("Rodar Detecção de Objetos"):
        st.image("sample_yolo_output.jpg", caption="Resultado da Detecção", use_container_width=True)
