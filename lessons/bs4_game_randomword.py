import requests
from bs4 import BeautifulSoup
from googletrans import Translator  # pip install googletrans==3.1.0a0


translator = Translator()


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = translator.translate(soup.find("div", id="random_word").text.strip(), dest="ru").text
        # Получаем описание слова
        word_definition = translator.translate(soup.find("div", id="random_word_definition").text.strip(), dest="ru").text
        # Чтобы программа возвращала словарь
        return {
           "english_words": english_words,
           "word_definition": word_definition
        }
        # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("ERROR!")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Welcome to the Game")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"The meaning of the word is - {word_definition}")
        user = input("What is the word? ")
        if user == word:
            print("Correct!")
        else:
            print(f"No, the word was - {word}")

        # Создаём возможность закончить игру
        play_again = input("Again? y/n ")
        if play_again != "y":
            print("Thanks for playing!")
            break


word_game()
