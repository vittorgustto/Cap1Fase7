# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>


## Grupo 67

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/company/inova-fusca">João Vitor Lopes Beiro</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Thyego Brandão</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gabriel Alves Costa</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Ferreira Hillesheim</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

### Atividade Capítulo 1 - Fase 7 ###
Este projeto integra simulação de sensores agrícolas, automação de irrigação e visualização de dados em tempo real por meio de um painel interativo no Streamlit. Os dados simulados da plantação são capturados no Wokwi com o ESP32 e enviados ao banco de dados, sendo posteriormente consumidos pela aplicação em Python. O objetivo é fornecer uma visão clara das condições da plantação e acionar ou desativar a irrigação de forma automatizada, de acordo com a umidade do solo.

### 📁 Estrutura e Explicação dos Arquivos ###

#### fase7_dashboard/dashboard_streamlit/app.py ####

Este é o arquivo principal do dashboard. Ele faz a conexão com o banco de dados e exibe os dados em tempo real, incluindo um gráfico com as variáveis de sensores e o status da irrigação.Principais funcionalidades:

 * Leitura dos dados mais recentes da tabela.

 * Visualização de gráfico com histórico de sensores.

 * Exibição do status atual da irrigação (ligada/desligada).

#### fase7_dashboard/adaptador.py ####

Este script atua como intermediador entre o monitor serial (onde os dados do ESP32 são exibidos) e o banco de dados. Ele lê os dados enviados pela porta serial e os insere automaticamente no banco.Funções principais:

 * Leitura da porta serial (COMx).

 * Conversão dos dados recebidos para dicionário.

 * Inserção no banco usando comandos SQL.

#### fase7_dashboard/fase2_bancodedados/fase2_codigo.py ####

ste é o script de criação e gerenciamento do banco de dados. Ele define a estrutura da tabela sensores, contendo colunas como umidade, temperatura, nivel_ph, nutriente_P, nutriente_K, data_hora e irrigacaoAtiva.Utilidade:

 * Criação inicial da tabela (caso não exista).

 * Pode ser usado para testes e consultas simples.

#### fase7_dashboard/fase2_bancodedados/conexao_db.py ####

Script com a função de conexão com o banco de dados SQLite. Ele é usado por outros scripts para realizar operações no banco (inserção, leitura).Principais elementos:

 * Função conectar() que retorna o cursor e a conexão ativa com o banco banco_sensores.db.

#### fase7_dashboard/fase2_bancodedados/gerar_dados_teste.py ####

Este script gera dados simulados para testar o banco de dados e a dashboard, sem depender do monitor serial.Destaques:

 * Geração aleatória de valores de sensores.

 * Inserção direta no banco de dados via conexao_db.py.

#### fase7_dashboard/fase2_bancodedados/consultar_dados.py ####

Script simples usado para consultar e imprimir os dados do banco no terminal, útil para verificação rápida.Permite:

 * Visualizar todas as linhas inseridas.

 * Fazer testes manuais antes de conectar à interface gráfica.


### Link Vídeo Youtube ###

[https://www.youtube.com/watch?v=uNdEICYmiR0](https://www.youtube.com/watch?v=7VVoP12z3hE)

### 📌 Observações ###

 * A comunicação com o ESP32 é feita manualmente via Monitor Serial (no Arduino IDE ou outro software).

 * Os dados são atualizados automaticamente no banco de dados e refletidos no dashboard em tempo real.

 * O projeto simula sensores via Wokwi, e pode ser adaptado para sensores físicos reais com o ESP32.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
