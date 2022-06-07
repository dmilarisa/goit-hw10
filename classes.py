from collections import UserDict


# Не дуже зрозуміло, нащо цей додатковий клас, проте за умовою завдання був потрібний, тому він тут є))
class Field:
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record():

    # Ініціалізуємо запис, щоб в ній зберігалися обов'язковий параметр ім'я, необов'язковий телефон, а також створюємо список з об'єктів - телефонів
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone is not None:
            self.phones.append(phone.value)

    # Фукція для додавання нового телефону для юзера
    def add_phone(self, ph: Phone):
        self.phones.append(ph.value)

    # Функція для зміни телефона на новий
    def change_phone(self, ph: Phone, new_ph: Phone):
        i = 0
        while i < len(self.phones):
            if self.phones[i] == ph.value:
                self.phones[i] = new_ph.value
                break
            else:
                i += 1


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        k, i = rec.name.value, rec
        self.data[k] = i
