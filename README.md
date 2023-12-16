# ChatGPT with your own data using LangChain 🦜️🔗

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
