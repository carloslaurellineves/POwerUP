import streamlit as st
from openai import OpenAI
from prompts import PROMPTS

st.set_page_config(
    page_title="POwerUp",  # Nome da aba do navegador
    page_icon="⚡",           # Ícone na aba do navegador
    layout="wide",            # Layout responsivo
)

# Configuração da chave da OpenAI na barra lateral
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

# Exibir título e descrição do assistente
st.title("✍️ Story Creator")
st.write("Aqui você pode conversar sobre épicos, histórias e tarefas!")

# Inicializar o histórico específico do assistente no session_state
ASSISTANT_ID = "epic_story_task" # ID único para o assistente
selected_prompt = PROMPTS[ASSISTANT_ID] # Prompt selecionado

if ASSISTANT_ID not in st.session_state:
    st.session_state[ASSISTANT_ID] = [
        {"role": "system", "content": selected_prompt},
        {"role": "assistant", "content": "No que posso te ajudar?"}
    ]

# Exibir mensagens anteriores (exceto a system message)
for msg in st.session_state[ASSISTANT_ID]:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Input do usuário
user_input = st.chat_input("Digite sua pergunta ou solicitação:")

if user_input:
    if not openai_api_key:
        st.info("⚠️ Insira sua OpenAI API key para continuar.")
        st.stop()

    # Adicionar a pergunta do usuário ao histórico
    st.session_state[ASSISTANT_ID].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Criar cliente da OpenAI e gerar resposta
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state[ASSISTANT_ID]
    )

    msg = response.choices[0].message.content

    # Adicionar a resposta do assistente ao histórico
    st.session_state[ASSISTANT_ID].append({"role": "assistant", "content": msg})

    # Exibir a resposta
    with st.chat_message("assistant"):
        st.write(msg)   