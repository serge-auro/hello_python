import random
import arithmetic as aa

#1. Напишите скрипт, который запрашивает у пользователя текст, а затем записывает этот текст в файл user_data.txt.
string1 = ""
file = open("my_test_file.txt","w",encoding="utf-8")
while True:
    string1 = input("Пишем файл (завершить - exit)\n")
    if string1 == "exit":
        file.close()
        break
    else:
        file.write(string1+"\n")
file = open("my_test_file.txt","r",encoding="utf-8")
print("#1 ваш файл:\n",file.read())
file.close()

#2. Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление. Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.
a = 4
b = 7
print(f"a = {a}, b = {b}")
print("#2 умножение, деление, сложение, вычитание: ",
      aa.multiplication(a, b),
      aa.division(a, b),
      aa.addition(a, b),
      aa.subtraction(a, b))


#3. Напишите программу, которая эмулирует выбор без повторений: из списка учащихся класса программа случайным образом выбирает 5 уникальных имён, которые будут отвечать на уроке. Имена учащихся считываются заранее из входного списка и не должны повторятся.

list1 = ["Serge", "Ivan", "Igor", "Ilya", "Vladimir", "Vitaly", "Kate", "Ann"]
print("#3 Выбор 5 учеников:", random.sample(list1, 5))
