import os 
import sys 

from apikey import apikey
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(options=chrome_options)


def fetch_amazon_review(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    review_elements = driver.find_elements("css selector", "div[data-hook='review']")
    total = 0
    reviews = []
    
    for review_element in review_elements:
        text = review_element.find_element("css selector","span[data-hook='review-body']").text.strip()
        total += len(text)
        if total < 2000:
          reviews.append(text)

    driver.quit()
    return reviews

def scrape_amazon_reviews(product_id):
    base_url = f"https://www.amazon.com/product-reviews/{product_id}?pageNumber="
    current_page = 1
    all_reviews = []

    while True:
        if current_page > 5: 
            break
        url = base_url + str(current_page)
        reviews = fetch_amazon_review(url)
        if not reviews:
            break
        all_reviews.extend(reviews)
        current_page += 1

    return all_reviews

import re

def get_product_id(current_url):
  pattern = r"https?://(?:www\.)?amazon\.com/.*/(dp|gp/product)/(.*?)(/|\?|$)"
  match = re.match(pattern, current_url)

  if match != None: 
    url_parts = current_url.split('/')
    product_id = url_parts[5]
    return product_id


# user_url = input("Input URL:")
# product_id = get_product_id(user_url)

# reviews = scrape_amazon_reviews(get_product_id(current_url))


from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


os.environ["OPENAI_API_KEY"] = apikey

llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=apikey)

template = """
%INSTRUCTIONS:
Summarize the following list of product reviews 
by giving a brief review of the common complaints or
satisfactions with the product. 

%TEXT:
{list}
"""

prompt = PromptTemplate(
    input_variables=["list"],
    template=template,
)

# final_prompt = prompt.format(list=reviews)
# output = llm(final_prompt)







