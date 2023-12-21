# ChatGPT with your own data using LangChain 🦜️🔗
## Your data, your ChatGPT. LangChain makes it happen
This repository empowers you to break free from generic AI and build your own personalized ChatGPT model.  Leveraging the flexibility of LangChain, you can train ChatGPT on your own data, be it code, documents, emails, or any text format that sparks your imagination. ✨
A powerful process where you can leverage the capabilities of ChatGPT, a popular generative AI model, and tailor its responses to your specific needs using LangChain, a versatile data integration and manipulation tool.
### ChatGPT models:
| Models   | MODEL FAMILIES	| API ENDPOINT |
| -------- | -------- | -------- |
| Newer models (2023–)| gpt-4, gpt-4 turbo, gpt-3.5-turbo	 | https://api.openai.com/v1/chat/completions |
| Updated legacy models (2023)	 | gpt-3.5-turbo-instruct, babbage-002, davinci-002	 | https://api.openai.com/v1/completions |
| Legacy models (2020–2022)	 | text-davinci-003, text-davinci-002, davinci, curie, babbage, ada | https://api.openai.com/v1/completions |

ChatGPT models, including GPT-3.5-turbo and its predecessors, are part of the GPT family of models developed by OpenAI. Here are some key features of ChatGPT models:

* Generative Pre-trained Transformer (GPT) Architecture.
* Conversational Nature.
* Versatility in Natural Language Processing (NLP) Tasks.
* API Access.
* Contextual Understanding.

### LangChain 🦜️🔗 Benifits:
It provide you with various loaders for different platforms and data types, such as GitHub repositories, PDF files, HTML content, APIs, social media, databases, and more. Each loader is designed for a specific purpose, making it versatile for handling diverse document-loading scenarios:
<pre> 
from langchain.document_loaders import DirectoryLoader, WebBaseLoader, TextLoader, PyPDFLoader, GitLoader, CSVLoader, PythonLoader
</pre>
# To Use:
* Clone repository.
* Make sure python == 3.10.12 is installed, if not:
<pre>
  sudo apt update
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install python3.10
</pre>
* Download requirements.txt:
<pre>
  pip install requirements.txt
</pre>
* In constant.py, you should replace "YOUR API KEY" with your own OpenAI API Key https://platform.openai.com/account/api-keys
  <pre>
    APIKEY = "YOUR API KEY"
  </pre>
### Test:
* After setting up the environment and after running the python file, a prompt will pop up.
  <pre>
    Prompt:
  </pre>
* In Data folder, there is a sample data.txt, which contains an article about AI, and a cat.pdf which contains a line "My cat's name is Muffy."
  <pre>
    Prompt: What is my cat's name?
  </pre>  
  And the result will be:
  <pre>
    Prompt: What is my cat's name?
    Your cat's name is Muffy.
  </pre>
* For summerization we will test the data.txt file.
  <pre>
    Select:
    1- PDF File.
    2- WebPage.
    3- TXT File.
    0 To Exit ==> 3
  </pre>
  <pre>
    Your TXT File Name ==> data.txt
  </pre>
  The result will be:
  <pre>
    Summarized Text:
    Artificial Intelligence (AI) has revolutionized various industries, with Natural Language Processing (NLP) and Large 
    Language Models (LLMs) gaining significant attention. ChatGPT, a creation of OpenAI, is a remarkable LLM that showcases 
    advanced language understanding and generation capabilities. NLP focuses on enabling machines to comprehend and generate 
    human-like language, while LLMs like GPT-3 and ChatGPT have shown exceptional language understanding and generation 
    capabilities. ChatGPT has applications in conversational agents, content generation, and programming assistance, but challenges 
    such as bias and ethical concerns need to be addressed. Overall, AI, NLP, and LLMs represent the forefront of technological 
    innovation, with responsible development and ethical considerations playing a crucial role in harnessing their full potential 
    for the benefit of society.
  </pre>
  ---------------------------------------------------------------------------------
  ## Collaborators

- [![Haitham-Wahhdan](https://github.com/Haitham-Wahhdan.png)](https://github.com/Haitham-Wahhdan).
