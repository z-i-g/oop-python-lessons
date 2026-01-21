# 2
class Application: # заявка
    app_no = '123' # номер заявки
    amount = 3000000 # запрошенная сумма
    decision = "Одобрена" # решение по заявке

    def __init__(self, app_no, amount, decision):
        self.app_no = app_no
        self.amount = amount
        self.decision = decision

    def increase_amount(self, added_amount):
        self.amount += added_amount

    def reduce_amount(self, decreasing_amount):
        if (self.amount >= decreasing_amount):
            self.amount -= decreasing_amount

    def change_decisio(self, new_decision):
        self.decision = new_decision

    
from datetime import date, timedelta
class Participant: # участник
    def __init__(self, person_num, first_name, second_name, last_name, age, birth_date, id_num, id_series):
        self.person_num = person_num
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age
        self.id_num = id_num
        self.id_series = id_series
        self.birt_date = birth_date

    def change_perso_num(self, new_person_num):
        self.person_num = new_person_num

    def check_age(self):
        return date.today() - self.birt_date != self.age
    
    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

class Document:
    def __init__(self, type, num, sign_date, sign_first_name, sign_second_name, sign_last_name):
        self.type = type
        self.num = num
        self.sign_date = sign_date
        self.sign_first_name = sign_first_name
        self.sign_second_name = sign_second_name
        self.sign_last_name = sign_last_name

    def change_type(self, new_doc_type):
        self.type = new_doc_type

    def check_valid_sig_date(self):
        return date.today() - self.sign_date > timedelta(days=5)
    
document = Document('FinDoc', 1, 2026-1-19, 'FirstName', 'SecondName', 'LastName')
document.change_type('AdditionalDoc')
print(document.type)
print(document.check_valid_sig_date())