import codecs
import os

class UIDict(dict):
    def __init__(self, val=None):
        if val is None:
            val = {}
        super().__init__(val)


    def __setitem__(self, item, value):
        f = codecs.open(value, 'r', 'utf-8')
        super().__setitem__(item, f.read())
        f.close()


    def __getitem__(self, item):
        value = super().__getitem__(item)
        return value
       # return lambda x, y: x + y

    def __delitem__(self, item):
        super().__delitem__(item)

UI = UIDict()
UI['button-list'] = "/home/julia/web/python/templates/button-template.html"
# render(
#         request,
#         'index.html', context={'notes': notes_serialized,
#                                'history': history_serialized})

print(UI['button-list'])




# print(f)
# print(UI)
# print(UI.changed)
# print(UI)

# UI["button-list"]="resource/button-template.html"

# component = UI["button-list"]
#    component(correct="Yes", bad="no")
