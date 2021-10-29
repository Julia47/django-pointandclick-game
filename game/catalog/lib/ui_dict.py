from jinja2 import Template
import codecs
import os
# settings_dir = os.path.dirname(__file__)
# PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
# XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'xml_files/')



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
        template = Template(value)
        return lambda **kwargs: template.render(kwargs)

    def __delitem__(self, item):
        super().__delitem__(item)

print(os.path)
UI = UIDict()
UI['buttons-template'] = '/home/julia/web/python/django-pointandclick-game/game/catalog/lib/templates/buttons-template.html'
# UI['checkboxes-template'] = 'game/catalog/lib/templates/checkboxes-template.html'
# UI['input-template'] = 'game/catalog/lib/templates/input-template.html'
# test = UI['buttons-template']

# print(settings_dir)
print(os.path.abspath(os.path.dirname('.')))
