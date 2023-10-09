import os 
import sys 

from apikey import apikey
import openai 
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI 
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = apikey

PERSIST = False

query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  from langchain.indexes.vectorstore import VectorStoreIndexWrapper
  index = vectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = TextLoader('data.txt')
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs=
    {"perisist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = RetrievalQA.from_chain_type(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k":1})
)

print(chain.run(query))

