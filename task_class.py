# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
from random import randint

STATUS = ('CREATED', 'IN PROGRESS', 'DONE')

class Task():

    def __init__(self, description, date):
        self.description = description
        self.date = date
        self.status = 'CREATED'

    def in_progress(self):
        self.status = 'IN PROGRESS'

    def done(self):
        self.status = 'DONE'


tasks = [Task('just fun', "2024/04/04"), Task('Hell the World', "2024/04/04"), Task('Do smt new', "2024/04/04")]

curr = randint(0, len(tasks)-1)
tasks[curr].in_progress()
curr = randint(0, len(tasks)-1)
tasks[curr].done()

for task in tasks:
    if task.status == 'IN PROGRESS':
        print(task.description)
