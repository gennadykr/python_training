from sys import maxsize
import re


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "(id:%s,name:%s,header:%s,footer:%s)" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clean(self):
        name = self.name.strip()
        name = re.sub('  ', ' ', name)
        return Group(id=self.id, name=name)