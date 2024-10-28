AI Web Scraper - Use AI To Scrape ANYTHING

First download the requirements.txt file and install the dependencies.

```
pip install -r requirements.txt
```

Then in main.py:
1. we will start with building the UI with streamlit.
2. Grab data from the website that we want to scrape using Selenium then pass it to a LLM.
3. Clean the data using LangChain.
4. Use OLLAMA to run the LLM.
5. Display the data in the UI.
