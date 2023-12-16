from langchain.chains.summarize import load_summarize_chain, _load_stuff_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
import constants
import os

# Specify the path to the PDF document
pdf_text = "/media/kamikaze/New Volume/chatgpt-retrieval-main/chatgpt-retrieval-main/data/AIM_DOCUMENTATION.pdf"

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Load the PDF document
loader = PyPDFLoader(pdf_text)
docs = loader.load()

# Create a ChatOpenAI model
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

# Create a summarization chain
summarization_chain = load_summarize_chain(llm, chain_type="stuff")

# Create a stuff chain with a specific document variable name
# Use 'text' as the document variable name internally
chain2 = _load_stuff_chain(llm, document_variable_name="text")

# Run the summarization chain on the documents
summarized_result = summarization_chain.run(docs)

# Run the stuff chain on the documents with the internal variable name
stuff_result = chain2.run(docs)

# Print the summarized text from both chains
print("Summarized Text (Summarization Chain):")
print(summarized_result)

print("\nSummarized Text (Stuff Chain):")
print(stuff_result)
