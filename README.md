# ChatGPT with your own data using LangChain 🦜️🔗

### ChatGPT models:
|          | MODEL FAMILIES	| API ENDPOINT |
| -------- | -------- | -------- |
| Newer models (2023–)| Row 1, Col 2 | Row 1, Col 3 |
| Updated legacy models (2023)	 | Row 2, Col 2 | Row 2, Col 3 |
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
