# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
#        self._User__access_level = 'admin' # Mangling
        self.set_access_level('admin')

    def add_user(self, users, id, name, access_level):
        if access_level == 'admin':
            user = Admin(id, name)
            user.set_access_level(access_level)
        else:
            user = User(id, name)
        users.append(user)

    def del_user(self, users, id):
        id_to_del = -1
        curr_id = 0
        for user in users:
            curr_id += 1
            if user.get_id() == id:
                id_to_del = curr_id
        users.pop(id_to_del)

    def print_users(self, users):
        for user in users:
            print(f'user {user.get_id()} name: {user.get_name()}; access_level: {user.get_access_level()}')


## MAIN ##
users = [User(1, 'Mary'), User(2, 'Carl'), Admin(3, 'Dmitry')]

users[2].add_user(users, 4, 'Nelly', 'admin')
users[2].print_users(users)
print("DELETION OF USERS")
users[2].del_user(users,3)
users[2].print_users(users)

