# Amazon-Review-Summarizer

This Python script utilizes Selenium for web scraping to collect Amazon product reviews and OpenAI's GPT-3.5 for natural language processing to summarize the gathered reviews. The process involves fetching reviews from multiple pages of a specified product on Amazon and then summarizing the common sentiments including complaints.

## Installation 

Install [Langchain](https://github.com/langchain-ai/langchain) and other required packages 

Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

## Example usage 

Run summaryGUI.py 

`python3 summaryGUI.py`

Input a URL from any Amazon product 

<img width="485" alt="guipic" src="https://github.com/jusrusswebb/review-summarizer/assets/122849382/544fff56-227e-4c04-ba8b-a31c4d4899f4">



Lets see what the reviews of this [INSE Cordless Vacuum](https://www.amazon.com/INSE-Cordless-Lightweight-Rechargeable-Powerful/dp/B0CHFBC9B5/ref=sr_1_3?crid=2DPT79P1ZLO02&keywords=INSE+Cordless+Vacuum&qid=1702424870&s=home-garden&sprefix=inse+cordless+vacuum%2Cgarden%2C184&sr=1-3) have to say... 


`The reviews generally indicate that this product is good for hardwood and low pile carpets, is lightweight and easy to maneuver, and has good suction. However, it is not suitable for thick carpets, the battery life is not very long, and the dust collection unit can be difficult to assemble. Additionally, the filters need to be cleaned frequently and the charger may stop working.`

Hmmm, I think I'm looking for an option better suited for carpet, lets try this [BISSELL Swivel Vacuum](https://www.amazon.com/BISSELL-Cleanview-Upright-Bagless-2252/dp/B07F6N3RT6/ref=sr_1_5?crid=1R75T4U8RAR1V&keywords=vacuum%2Bfor%2Bthick%2Bcarpet&qid=1702425304&s=home-garden&sprefix=vaccuum%2Bfor%2Bthick%2Bcarp%2Cgarden%2C236&sr=1-5&th=1)

`The reviews for this Bissell vacuum are overwhelmingly positive, with customers praising its strong suction power, ease of use, and affordability. The only common complaint is that the suction tank is difficult to empty, requiring users to reach in and pull out debris. Other than that, customers are highly satisfied with the product and recommend it to others.`
