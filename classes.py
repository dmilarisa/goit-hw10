from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record(UserDict):

    def __init__(self, name: Name, phone: Phone = None):
        super().__init__(self)
        self.data['name'] = name.value
        self.data['phones'] = []
        self.data['phones'].append(phone.value)

    def add_phone(self, ph: Phone):
        self.data['phones'].append(ph.value)

    def change_phone(self, ph:Phone, new_ph:Phone):
        i = 0
        while i < len(self.data['phones']):
            if self.data['phones'][i] == ph.value:
                self.data['phones'][i] = new_ph.value
                break
            else:
                i += 1


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        k, i = rec['name'], rec
        # k, i = rec.name.value, rec.phones
        self.data[k] = i
