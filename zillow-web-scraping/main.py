from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdF3Z9axNBD9uDPVhRTm9GwUl54VieHHzxPARKSxylBRMJAkQ/viewform"
url = "https://appbrewery.github.io/Zillow-Clone/"

def clean_price(price_text):
    cleaned_price = re.sub(r'[^0-9.]', '', price_text)
    return f"${cleaned_price}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", class_="property-card-link")
links_list = [link.get("href") for link in links]

price_elements = soup.find_all("span", attrs={"data-test": "property-card-price"})
# Clean prices and store them in a list
prices_list = [clean_price(price.get_text(strip=True)) for price in price_elements]

addresses = soup.find_all("address")
addresses_list = [address.get_text(strip=True) for address in addresses]

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get(form_url)
time.sleep(3)

# Loop through each property (address, price, link) and fill in the form
for address, price, link in zip(addresses_list, prices_list, links_list):
    # Fill the address field
    first_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_field.send_keys(address)

    # Fill the price field
    second_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_field.send_keys(price)

    # Fill the link field
    third_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_field.send_keys(link)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(1)

    # Optionally, navigate back to the form for the next submission (if the form reloads)
    driver.get(form_url)
    time.sleep(2)

# Close the WebDriver after all submissions
driver.quit()
