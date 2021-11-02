from jinja2 import Template
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
        template = Template(value)
        return lambda **kwargs: template.render(kwargs)

    def __delitem__(self, item):
        super().__delitem__(item)


UI = UIDict()
UI['buttons-template'] = (os.path.join('catalog', 'lib', 'templates',
                                       'buttons-template.html'))
UI['checkboxes-template'] = (os.path.join('catalog', 'lib', 'templates',
                                          'checkboxes-template.html'))
UI['input-template'] = (os.path.join('catalog', 'lib', 'templates',
                                     'input-template.html'))
