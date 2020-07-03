# -*- coding:utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self.contacts:
            self.printContact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self.contacts):
            if (contact.name.lower() == name.lower()):
                del self.contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self.contacts:
            if (contact.name.lower() == name.lower()):
                self.printContact(contact)
                break
        else:
            self._notFound()

    def _save(self):
        with open('contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self.contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def update(self, oldName, newName, newPhone, newEmail):
        for contact in self.contacts:
            if (contact.name.lower() == oldName.lower()):
                contact.name = newName
                contact.phone = newPhone
                contact.email = newEmail
                self.printContact(contact)
                break
        else:
            self._notFound()


    def printContact(self, contact):
        print('---- * ---- * ---- * ---- * ---- * ---- * ----')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---- * ---- * ---- * ---- * ---- * ---- * ----')

    def _notFound(self):
        print('¡Contacto no encontrado!')

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if (idx == 0):
                continue
            
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
        ¿Qué desea hacer? 

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]listar contactos 
        [s]alir
        '''))

        if (command == 'a'):
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif (command == 'ac'):
            name = str(input('Escribe el nombre del contacto a actualizar'))

            newName = str(input('Nuevo nombre: '))
            newPhone = str(input('Nuevo teléfono: '))
            newEmail = str(input('Nuevo email: '))

            contact_book.update(name, newName, newPhone, newEmail)

        elif (command == 'b'):

            name = str(input('Escribe el nombre del contacto: '))

            contact_book.search(name)

        elif (command == 'e'):
            
            name = str(input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif (command == 'l'):
            
            contact_book.show_all()

        elif (command == 's'):
            
            print('Salir')
            break

if __name__ == "__main__":
    run()