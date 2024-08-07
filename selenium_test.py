import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Specify the URL
url = "https://www.divan.ru/category/svet"

# Open the web page
driver.get(url)

# Wait for the lamps to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, '_Ud0k'))
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# Find all lamp cards
lamps = driver.find_elements(By.CLASS_NAME, '_Ud0k')

# Output the number of lamps found
print(f"Found {len(lamps)} lamps.")

# Create a list to store parsed data
parsed_data = []

# Iterate over each lamp card
for lamp in lamps:
    try:
        # Find elements within each lamp
        try:
            name = lamp.find_element(By.CSS_SELECTOR, 'div.lsooF a span').text
        except NoSuchElementException:
            name = 'Not specified'
        try:
            price = lamp.find_element(By.CSS_SELECTOR, 'div.pY3d2 span[data-testid="price"]').text
        except NoSuchElementException:
            price = 'Not specified'
        try:
            link = lamp.find_element(By.CSS_SELECTOR, 'div.lsooF a').get_attribute('href')
        except NoSuchElementException:
            link = 'Not specified'

        # Append the found information to the list
        parsed_data.append([name, price, link])
    except NoSuchElementException as e:
        print(f"Error parsing lamp: {e}")
        continue

# Close the browser
driver.quit()

# Write the data to a CSV file
with open("lamp.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'price', 'url'])
    writer.writerows(parsed_data)
