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
url = "https://tomsk.hh.ru/vacancies/programmist"

# Open the web page
driver.get(url)

# Wait for the vacancies to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y'))
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# Find all vacancy cards
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

# Output the number of vacancies found
print(f"Found {len(vacancies)} vacancies.")

# Create a list to store parsed data
parsed_data = []

# Iterate over each vacancy card
for vacancy in vacancies:
    try:
        # Find elements within each vacancy
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        try:
            company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        except NoSuchElementException:
            company = 'Not specified'
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
        except NoSuchElementException:
            salary = 'Not specified'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')

        # Append the found information to the list
        parsed_data.append([title, company, salary, link])
    except NoSuchElementException as e:
        print(f"Error parsing vacancy: {e}")
        continue

# Close the browser
driver.quit()

# Write the data to a CSV file
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)