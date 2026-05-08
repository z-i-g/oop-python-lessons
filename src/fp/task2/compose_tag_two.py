from pymonad.reader import Compose
from pymonad.tools import curry

@curry(2)
def tag(tag_name, tag_value):
    return f"<{tag_name}>{tag_value}</{tag_name}>"

bold = tag('b')
italic = tag('i')

bold_and_italic = Compose(bold).then(italic)

print(bold_and_italic('Hello'))