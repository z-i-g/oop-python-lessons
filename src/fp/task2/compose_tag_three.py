from pymonad.tools import curry
from pymonad.reader import Compose

@curry(3)
def tag(tag_name, tag_attrs, tag_value):
    attrs_string = "".join([f' {k}="{v}"' for k, v in tag_attrs.items()])
    return f"<{tag_name}{attrs_string}>{tag_value}</{tag_name}>"

bold_red = tag('b', {'style': 'color: red'})
li_item = tag('li', {'class': 'list-group'})

complex_tag = Compose(bold_red).then(li_item)

print(complex_tag("Hello"))