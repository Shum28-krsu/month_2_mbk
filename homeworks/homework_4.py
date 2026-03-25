class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            raise ValueError("Номер телефона должен содержать ровно 10 цифр!")

ContactList.add_contact("Baibol", "0706899091")
ContactList.add_contact("Aian", "0706899092")
ContactList.add_contact("Bakas", "0706899093")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

