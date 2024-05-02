import streamlit as st

import google.generativeai as gen_ai


GOOGLE_API_KEY = "API KEY"

gen_ai.configure(api_key=GOOGLE_API_KEY)
king = gen_ai.GenerativeModel()


def translate_role_for_streamlit(user_role):
    if user_role == "king":
        return "👑"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = king.start_chat(history=[])

st.title("👑 KING - ChatBot")


for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


user_prompt = st.chat_input("HEY KING WHAT YOU WANT......")
if user_prompt:
  
    st.chat_message("user").markdown(user_prompt)

    king_response = st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("👑"):
        st.markdown(king_response.text)