import streamlit as st

st.set_page_config(
    page_title="POwerUp",  # Nome da aba do navegador
    page_icon="⚡",           # Ícone na aba do navegador
    layout="wide",            # Layout responsivo
    initial_sidebar_state="expanded"  # Abre o menu lateral por padrão
)

st.title('POwerUp ⚡')
st.header('O Assistente Definitivo para POs!')

st.write('Seu boost de produtividade para escrever épicos incríveis, estimar esforços e garantir que nada passe sem critérios de aceitação bem definidos.')

st.markdown('''
Seja bem-vindo ao **POwerUp**, seu copiloto na jornada de transformar ideias em épicos bem estruturados, histórias incríveis e tarefas bem definidas! 🎯✨  Aqui, você não precisa mais lutar contra backlogs desorganizados ou histórias vagas – o **POwerUp** veio para dar aquele *boost* na sua produtividade! 💡⚡  

## 🗺️ O que você encontra por aqui?

### ✍️ **Story Creator**  
Diga adeus às especificações confusas! Com o **POwerUp**, você pode criar épicos detalhados, histórias bem escritas e tarefas organizadas para manter seu time alinhado. 🚀  

### 📊 **Dimensionamento de Esforço**  
Está na dúvida sobre a complexidade de uma história? Nosso assistente ajuda a estimar o esforço necessário, seja em *story points*, T-shirt sizes ou na sua métrica favorita! 📏👕

### 🔍 **Cenários de Teste & Critérios de Aceitação**  
Nada de *deploy* com surpresa! O **POwerUp** gera cenários de teste e critérios de aceitação bem definidos, garantindo que tudo esteja pronto para a próxima sprint. ✅🔄  

### 📚 **Dicas & Melhores Práticas**  
Quer aprimorar sua escrita de histórias? Aprender mais sobre métricas ágeis? Nosso assistente traz dicas e boas práticas para você se tornar um PO *level máximo*! 🎮🔥  

## 🎯 Preparado para dar o **POwerUp**⚡ no seu backlog?  
Vamos juntos transformar requisitos em histórias épicas e sprints bem-sucedidas! 🌟✨    
            ''')
