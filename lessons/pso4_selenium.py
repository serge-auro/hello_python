from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        time.sleep(1)
        assert "Wikipedia" in self.driver.title
        self.paragraphs = []
        self.current_paragraph_index = 0

    def get_search(self, query):
        search_icon = self.driver.find_element(By.CLASS_NAME, "mw-ui-icon-wikimedia-search")
        search_icon.click()
        time.sleep(1)
        search_box = self.driver.find_element(By.NAME, "search")
        time.sleep(1)
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        self.paragraphs = self.driver.find_elements(By.TAG_NAME, "p")
        self.current_paragraph_index = 0

    def print_next_paragraph(self):
        if self.current_paragraph_index < len(self.paragraphs):
            paragraph = self.paragraphs[self.current_paragraph_index]
            print(paragraph.text)
            self.current_paragraph_index += 1
        else:
            print("No more paragraphs in this article.")

    def get_random_link(self):
        hatnotes = []
        for element in self.driver.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        if hatnotes:
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            return link
        else:
            print("No related articles found.")
            return None

    def go_to_link(self, link):
        if link:
            self.driver.get(link)
            time.sleep(2)
            self.paragraphs = self.driver.find_elements(By.TAG_NAME, "p")
            self.current_paragraph_index = 0
        else:
            print("Invalid link")


def main():
    driver = Driver()
    while True:
        query = input("What do you want to search for? (type 'exit' to exit) \n")
        if query.lower() == 'exit':
            break
        driver.get_search(query)
        while True:
            action = input("Choose an action: 'next' to see next paragraph, "
                           "\n'link' to follow a related link, "
                           "\n'new' to start a new search, 'exit' to exit: \n").lower()
            if action == 'exit':
                return
            elif action == 'next':
                driver.print_next_paragraph()
            elif action == 'link':
                link = driver.get_random_link()
                if link:
                    driver.go_to_link(link)
                    break
            elif action == 'new':
                break
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
