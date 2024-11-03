import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def chat_page():
    st.subheader("Health Assistant", divider='grey')
    st.caption("Access your API key from your [OpenAI account](https://platform.openai.com/api-keys)")
    st.markdown("")
    st.caption("Go ahead, ask me anything!")

    # Use the API key from the environment variable
    api_key = os.getenv("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")

    if api_key:
        openai.api_key = api_key
        user_input = st.text_input("Ask a health-related question:")

        if st.button("Get Answer"):
            try:
                response = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt=user_input,
                    max_tokens=150
                )
                st.text("Chatbot's Response:")
                st.text(response.choices[0].text.strip())
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.error("API key not found. Please set it in the .env file.")

if __name__ == "__main__":
    chat_page()
