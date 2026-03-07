class AbstractCleaner:

    # режимы работы устройства очистки
    WATER = 1 # полив водой
    SOAP  = 2 # полив мыльной пеной
    BRUSH = 3 # чистка щётками

    def __init__(self):
        pass

    # перемещение
def move(transfer,dist,state):
    pass

# поворот
def turn(transfer,turn_angle,state):
    pass

# установка режима работы
def set_state(transfer,new_internal_state,state):
    pass

# начало чистки
def start(transfer,state):
    pass

# конец чистки
def stop(transfer,state):
    pass

# интерпретация набора команд
def make(transfer,code,state):
    pass