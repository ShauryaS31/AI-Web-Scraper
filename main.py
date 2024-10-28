import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter the Website URL: ")

if st.button("Scrape Data"):
   st.write("Scraping data from the website...")
   result = scrape_website(url)
   print(result)

