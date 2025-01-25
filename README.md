# Generative AI Playground

## Overview
**Generative AI Playground** is a user-friendly web application built with Streamlit, designed to demonstrate text generation using pre-trained language models from Hugging Face. Users can experiment with various models, configure generation settings, and experience the magic of AI-driven text generation.

---

## Features
- **Model Selection**: Choose from pre-trained models such as:
  - `google/gemma-2-27b-it`
  - `meta-llama/Meta-Llama-3-8B-Instruct`
  - `HuggingFaceTB/SmolLM2-1.7B-Instruct`
- **Customizable Parameters**:
  - Set **maximum tokens** for output length.
  - Adjust **temperature** to control randomness in generation.
- **Interactive User Interface**:
  - Input a prompt and generate responses instantly.
  - Real-time feedback on model-generated text.

---

## Getting Started

### Prerequisites
- Python 3.8 or above
- Hugging Face API token
- Required Python libraries (listed in `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/generative-ai-playground.git

2. Navigate to the project directory:
   ```bash
    cd generative-ai-playground

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

### Setting Up `secrets.toml`
Before running the app, create a `.streamlit/secrets.toml` file in the project directory and add your Hugging Face API token:
    ```toml
    # .streamlit/secrets.toml
    HUGGINGFACEHUB_API_TOKEN = "your_api_token"

### Running the App
Start the Streamlit app with the following command:
    ```bash
    streamlit run app.py

