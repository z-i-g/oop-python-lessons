from pymonad.tools import curry
from pymonad.reader import Compose

@curry(3)
def tag(tag_name, tag_attrs, tag_value):
    attrs_string = "".join([f' {k}="{v}"' for k, v in tag_attrs.items()])
    return f"<{tag_name}{attrs_string}>{tag_value}</{tag_name}>"

# 1. Подготавливаем функции через частичное применение
# Теперь bold_red и li_item — это функции, которые ждут только последний аргумент (value)
bold_red = tag('b', {'style': 'color: red'})
li_item = tag('li', {'class': 'list-group'})

# 2. Создаем цепочку с помощью Compose
# Текст сначала попадет в bold_red, а результат — в li_item
complex_tag = Compose(bold_red).then(li_item)

# 3. Проверка
print(complex_tag("Hello"))
# Результат: <li class="list-group"><b style="color: red">Внимание!</b></li>