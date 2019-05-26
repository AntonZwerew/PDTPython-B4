class Group():
    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = group_id

    def __repr__(self):
        return "%S:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name