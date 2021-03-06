# coding=utf-8
import time
import unittest

from pages.contact_adding_page import ContactAddingPage
from setup.default_setup import default_setup


class AddContactTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.page = ContactAddingPage(self.driver)

        self.page.open()

        self.dmitry_contact = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": ["d.boldin@corp.mail.ru"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }

        self.contact_with_many_emails = {
            "email": ["d.boldin@corp.mail.ru", "test@mail.ru"],
        }

        self.invalid_emails = [
            "это_имейл@mail.ru".decode('utf-8'),
            "email@email",
            "email.ru",
        ]

    def tearDown(self):
        self.page.open()

        self.page.delete_all_contacts()
        self.driver.quit()

    def test_adding_empty_contact(self):
        """
        Ошибка при добавлении контакта с пустыми полями
        """
        self.page.try_to_create_empty_contact()

        self.assertTrue(self.page.has_error())

    def test_invalid_email(self):
        """
         Ошибка при вводе невалидной почты
        """
        for email in self.invalid_emails:
            self.page.create_contact(close=False, email=[email])
            self.assertTrue(self.page.has_validation_errors())
            self.page.return_back()

    def test_contact_adding(self):
        """
        Проврека успешного создания контакта
        """

        self.page.create_contact(**self.dmitry_contact)
        self.page.open()
        self.assertTrue(self.page.contact_exists(self.dmitry_contact['email'][0]))

    def test_only_name(self):
        """
        Проверка создания контакта только с именем
        """

        self.page.create_contact(firstname=self.dmitry_contact["firstname"])
        self.page.open()

        self.assertFalse(self.page.has_any_error())

    def test_only_email(self):
        """
        Проверка создания контакта только с email
        """

        self.page.create_contact(email=self.dmitry_contact["email"])
        self.assertFalse(self.page.has_any_error())

    def test_latin(self):
        """
        Проверка создания контакта только с латинскими символами в имени
        """

        self.page.create_contact(nick="Some name")
        self.assertFalse(self.page.has_any_error())

    def test_unicode(self):
        """
        Проверка создания контакта с нетипичными unicode символами
        """

        self.page.create_contact(nick="ђћ∆".decode("utf-8"))
        self.assertFalse(self.page.has_any_error())

    def test_two_emails(self):
        """
        Проверка создания контакта с двумя email'ами
        """
        self.page.create_contact(**self.contact_with_many_emails)

        self.assertFalse(self.page.has_any_error())

    def test_same_contacts(self):
        """
        Проврека создания двух идентичных контактов
        """

        self.page.create_contact(**self.dmitry_contact)
        self.page.create_contact(close=False, **self.dmitry_contact)

        self.assertFalse(self.page.has_any_error())
