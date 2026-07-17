import streamlit as st
from chatbot import initialize_rag, chatbot

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="University Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- INITIALIZE RAG (CACHE) ----------------
@st.cache_resource
def load_system():
    initialize_rag()

load_system()

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main { background-color: #f7f9fc; }

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: #0b3d91;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 16px;
    margin-bottom: 20px;
}

.user-bubble {
    background: linear-gradient(90deg, #d1e7ff, #eaf4ff);
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    text-align: right;
}

.bot-bubble {
    background: #ffffff;
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    border-left: 5px solid #0b3d91;
}

.sidebar-title {
    font-size: 18px;
    font-weight: bold;
    color: #0b3d91;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🎓 University AI Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart answers for admissions, faculty, fees & more</div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)

    option = st.radio(
        "Select section:",
        ["💬 Chat", "📘 Admissions", "👨‍🏫 Faculty", "💰 Fees", "❓ FAQs"]
    )

    st.markdown("---")
    st.markdown("### ⚡ Quick Questions")

    def ask_quick(question):
        with st.spinner("Thinking..."):
            try:
                answer = chatbot(question)
            except Exception as e:
                answer = f"⚠️ Error: {e}"

        st.session_state.chat_history.append(("user", question))
        st.session_state.chat_history.append(("bot", answer))
        st.rerun()

    if st.button("Admission Criteria"):
        ask_quick("Admission criteria?")

    if st.button("Fee Structure"):
        ask_quick("Fee structure?")

    if st.button("Programs Offered"):
        ask_quick("Programs offered?")

# ---------------- PAGE MAP ----------------
page_map = {
    "📘 Admissions": "Tell me about admissions",
    "👨‍🏫 Faculty": "Tell me about faculty",
    "💰 Fees": "Tell me about fee structure",
    "❓ FAQs": "Show FAQs"
}

# ---------------- CHAT PAGE ----------------
if option == "💬 Chat":

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div class='user-bubble'>🧑 {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'>🎓 {msg}</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])

    with col1:
        user_input = st.text_input("Ask your question...", label_visibility="collapsed")

    with col2:
        send = st.button("Send ➤", use_container_width=True)

    if send and user_input:
        with st.spinner("Thinking..."):
            response = chatbot(user_input)

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))
        st.rerun()

# ---------------- OTHER PAGES ----------------
elif option in page_map:
    st.header(option)

    with st.spinner("Fetching information..."):
        answer = chatbot(page_map[option])

    st.success(answer)