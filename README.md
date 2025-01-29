# Text Generation using Hugging Face's model APIs

## Overview
This section of the **Generative AI Playground** is a user-friendly web application built with Streamlit, designed to demonstrate text generation using pre-trained language models from Hugging Face. Users can experiment with various models, configure generation settings, and experience the magic of AI-driven text generation.

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

### Tools used:
  - ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
  - ![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%94-green)
  - ![LangChain](https://img.shields.io/badge/LangChain-%E2%9C%94-blue)
  - ![Hugging Face](https://img.shields.io/badge/Hugging_Face-%E2%9C%94-blue)


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
    
    HUGGINGFACEHUB_API_TOKEN = "your_api_token"

### Running the App
Start the Streamlit app with the following command:
    
    streamlit run app.py

---

## Usage
  1. **Select a Model**: Use the dropdown menu to choose one of the pre-trained language models.
  2. **Configure Parameters**:
     - Adjust the **Max Tokens** slider to set the desired length of the generated text.
     - Set the **Temperature slider** to control the creativity of responses.
  3. **Input Prompt**: Enter a prompt in the text area, e.g., "Write a short story about hobbits."
  4. **Generate Text**: Click the "Generate Text" button to see the AI's response.


## Key Learnings
  - Experiment with different temperature and max token settings to fine-tune the balance between creativity and coherence in responses.
  - Use prompt engineering to improve the relevance and quality of generated outputs.



## Future Enhancements
  - Add more pre-trained models to the dropdown list.
  - Include additional configurable parameters like top_p and repetition_penalty.
  - Enable user-uploaded custom prompts for advanced use cases.



## Contributing
Contributions are welcome! Fork this repository, make changes, and submit a pull request. For major updates, open an issue to discuss your ideas.



## License
This project is licensed under the MIT License. See the LICENSE file for more details.



## Acknowledgments
  - Hugging Face: For providing accessible APIs and powerful pre-trained models.
  - Streamlit: For creating an intuitive framework for building web applications.
  - The open-source community for inspiration and tools.
