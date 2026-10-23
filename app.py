
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Manoel Grog",
    page_icon="🤖",
    layout="centered",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827 0%, #17283a 60%, #103b35 100%);
    color: #f4f7fb;
}
.main .block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.hero {
    padding: 1.5rem;
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 22px;
    background: rgba(255,255,255,.06);
    margin-bottom: 1.3rem;
}
.hero h1 { color: white; margin: 0; }
.hero p { color: #c7d4e5; margin-bottom: 0; }
.stChatMessage {
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🤖 Manoel Grog</h1>
  <p>Seu espaço de conversa com inteligência artificial.</p>
</div>
""", unsafe_allow_html=True)


# --------------------- SIDEBAR

with st.sidebar:
    st.title("⚙️ Configurações")
    st.caption("Modo de demonstração: somente front-end")
    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("Esta versão não está conectada a uma API.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Eu sou o Manoel Groq. Esta é uma demonstração visual da interface. 🤖"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Digite sua mensagem...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    demo_reply = "Sua mensagem apareceu na interface! Para gerar respostas reais, será necessário conectar um backend. 💬"
    st.session_state.messages.append({"role": "assistant", "content": demo_reply})
    with st.chat_message("assistant"):
        st.markdown(demo_reply)

