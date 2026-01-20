# 1.1
#Если взять в пример маркетплейс Озон, можно было бы выделить следующие классы:
#- Товар;
#- Корзина;
#- Пользователь;
#- Промокод и тд. 

# 1.2
class Application: # заявка
    app_no = '123' # номер заявки
    amount = 3000000 # запрошенная сумма
    decision = "Одобрена" # решение по заявке

class Participant: # участник
    person_num = 1 # номер участника
    first_name = 'Иван' # имя
    second_name = 'Петров' # фаммилия
    last_name = 'Петров' # отчество
    age = 21 # возраст
    id_num = 567890 # серия паспорта
    id_series = 1234 # номер паспорта

class Document:
    type = 'Finance' # тип документа
    num = '123' # номер
    sign_date = 21-12-2025 # дата подписания
    sign_first_name = 'Name' # Имя подписанта
    sign_second_name = 'Second Name' # Фамилия подписанта
    sign_last_name = 'Last Name' # Отчество подписанта

class Eployment:
    name = 'Sber' # имя работодателя
    inn = '123456789' # ИНН
    manager = 'Gref' # руководитель, начальник

# 1.3

application1 = Application()
application2 = application1

# если передать переменную application2 в функцию где произвести изменения
# application2.app_no = '321'
# то изменения произойдут в объекте Application созданным ранее