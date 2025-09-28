import streamlit as st
from bot import QABot

# Initialize bot (only once per session)
if "bot" not in st.session_state:
    st.session_state.bot = QABot()

st.title("🤖 Q&A Bot")
st.write("Ask me anything!")

# Input box
query = st.text_input("Your question:", "")

if query:
    with st.spinner("Thinking..."):
        answer = st.session_state.bot.ask(query)
    st.write(" Answer-> ")
    st.write(answer)

# Show history
if st.checkbox("Show conversation history"):
    for q, a in st.session_state.bot.show_history():
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
        st.markdown("---")
