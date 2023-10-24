# Import necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # Make sure you have Chrome webdriver installed

# Define the URL you want to scrape
url = "https://www.bbc.co.uk/news"  # Replace with your target URL

# Open the webpage using Selenium
driver.get(url)

# Get the page source and pass it to BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find and extract the relevant information
article_titles = soup.find_all('h3', class_='gs-o-bullet__icon ggs-c-promo-heading__title gel-canon-bold nw-o-link-split__text')  # Replace with actual HTML tags and classes

# Print the titles
for title in article_titles:
    print(title.text)

# Add a delay (in seconds) before quitting the WebDriver
time.sleep(10)  # This will wait for 10 seconds, adjust as needed

# Close the Selenium webdriver
driver.quit()
