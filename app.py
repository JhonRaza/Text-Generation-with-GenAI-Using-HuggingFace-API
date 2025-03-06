from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
import streamlit as st
from langchain.prompts import PromptTemplate


# App Header
st.title("Generative AI - Simple Text Generation")
st.markdown("""
This section of the **Generative AI Playground** app allows you to explore text generation with pre-trained language models from the Hugging Face model APIs. 
Just type in a prompt and let AI do the magic!
""")

# Sidebar for configuring the model
st.sidebar.title("Model Settings")
st.sidebar.text("🔗 Enter your Huggingface API Token")
token = st.sidebar.text_input("API Token", type="password")
button = st.sidebar.button("Save API Token")
if button:
    st.session_state.HUGGINGFACEHUB_API_TOKEN = token
    print(st.session_state.HUGGINGFACEHUB_API_TOKEN)
    st.sidebar.success("API Token saved successfully!")
    
st.sidebar.markdown("Configure the model settings for text generation.")
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=200, step=10)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)


# Dropdown to select the model
model_options = [
    "google/gemma-2-27b-it",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "HuggingFaceTB/SmolLM2-1.7B-Instruct",
]
columns = st.columns([2,2])
with columns[0]:
    selected_model = st.selectbox("Select a model for text generation:", model_options)

# Prompt input from the user
prompt = st.text_area("Enter your prompt:", placeholder="Write a short story about hobbits...")

# Button to trigger text generation
if st.button("Generate Text"):
    if "HUGGINGFACEHUB_API_TOKEN" not in st.session_state:
        st.error("Please enter your Hugging Face API Token.")
    else:
        hf_api_key = st.session_state.HUGGINGFACEHUB_API_TOKEN
        if prompt.strip() == "":
            st.error("Please enter a valid prompt.")
        else:
            # Configure the Hugging Face Hub LLM
            llm = HuggingFaceEndpoint(
                repo_id=selected_model,
                model_kwargs={"max_length": max_tokens},
                huggingfacehub_api_token=hf_api_key,
                temperature=temperature,
                )

            # Create a prompt template and chain
            template = "You are a helpful assistant designed to answer a user's queries. Answer the following user query precisely: |query| {input_text} |assistant|: "
            prompt_template = PromptTemplate(template=template, input_variables=["input_text"])
            chain = LLMChain(llm=llm, prompt=prompt_template)

            # Generate text
            generated_text = ""
            with st.spinner("Generating text..."):
                try:
                    generated_text = chain.invoke(input=prompt, verbose=True)
                    # print(generated_text['text'])
                    st.success("Generated Text:")
                    st.write(generated_text['text'])
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            print(generated_text)