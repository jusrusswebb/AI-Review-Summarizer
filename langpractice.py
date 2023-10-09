import os 
import sys 

from apikey import apikey
from langchain.llms import OpenAI
from langchain.document_loaders import HNLoader

os.environ["OPENAI_API_KEY"] = apikey

loader = HNLoader("https://www.amazon.com/product-reviews/0063226081?pageNumber=1")

data = loader.load()

print(len(data))













